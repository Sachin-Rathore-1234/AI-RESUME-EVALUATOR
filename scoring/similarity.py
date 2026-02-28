from sentence_transformers import SentenceTransformer
import numpy as np


# -------------------------------------------------------------------
# Domain knowledge: known equivalent / substitute technologies
# -------------------------------------------------------------------
TECH_EQUIVALENCE = {
    "kafka": ["aws kinesis", "azure event hubs", "google pubsub"],
    "aws kinesis": ["kafka"],
    "mysql": ["postgresql", "mariadb"],
    "postgresql": ["mysql"],
    "tensorflow": ["pytorch"],
    "pytorch": ["tensorflow"],
}


# -------------------------------------------------------------------
# Context enrichment for short / ambiguous skill tokens
# -------------------------------------------------------------------
SKILL_CONTEXT = {
    "kafka": "Apache Kafka distributed event streaming platform",
    "aws kinesis": "AWS Kinesis real-time data streaming service",
    "aws": "Amazon Web Services cloud computing platform",
    "docker": "Docker containerization platform",
    "microservices": "Microservices architecture for scalable systems",
    "python": "Python programming language",
}


class SemanticSimilarityScorer:
    """
    Computes semantic similarity between JD skills and resume skills
    using embeddings + domain-specific equivalence rules.
    """

    def __init__(self):
        # Lightweight, CPU-friendly embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    # ---------------------------------------------------------------
    # Normalize & enrich skill text before embedding
    # ---------------------------------------------------------------
    def _normalize(self, skill: str) -> str:
        return skill.strip().lower()

    def _enrich(self, skill: str) -> str:
        key = self._normalize(skill)
        return SKILL_CONTEXT.get(key, skill)

    # ---------------------------------------------------------------
    # Cosine similarity (manual for clarity)
    # ---------------------------------------------------------------
    def _cosine_similarity(self, vec1, vec2) -> float:
        return float(
            np.dot(vec1, vec2) /
            (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        )

    # ---------------------------------------------------------------
    # Domain equivalence check (Kafka ↔ Kinesis, etc.)
    # ---------------------------------------------------------------
    def _is_domain_equivalent(self, jd_skill: str, resume_skill: str) -> bool:
        jd = self._normalize(jd_skill)
        resume = self._normalize(resume_skill)
        return resume in TECH_EQUIVALENCE.get(jd, [])

    # ---------------------------------------------------------------
    # Main similarity computation
    # ---------------------------------------------------------------
    def compute_similarity_score(
        self,
        jd_skills,
        resume_skills,
        semantic_threshold=0.5
    ):
        """
        Returns:
        - similarity_score (0–100)
        - matched_pairs with explanation
        """

        # Enrich skills for better embeddings
        jd_texts = [self._enrich(s) for s in jd_skills]
        resume_texts = [self._enrich(s) for s in resume_skills]

        # Generate embeddings
        jd_embeddings = self.model.encode(jd_texts)
        resume_embeddings = self.model.encode(resume_texts)

        matched = []

        for i, jd_skill in enumerate(jd_skills):
            best_match = None
            best_score = 0.0

            for j, resume_skill in enumerate(resume_skills):
                score = self._cosine_similarity(
                    jd_embeddings[i],
                    resume_embeddings[j]
                )

                if score > best_score:
                    best_score = score
                    best_match = resume_skill

            # Decide match type
            if best_match:
                if best_score >= semantic_threshold:
                    match_type = "semantic"
                elif self._is_domain_equivalent(jd_skill, best_match):
                    match_type = "domain_equivalent"
                else:
                    match_type = None

                if match_type:
                    matched.append({
                        "jd_skill": jd_skill,
                        "resume_skill": best_match,
                        "similarity": round(best_score, 2),
                        "match_type": match_type
                    })

        similarity_score = (
            len(matched) / len(jd_skills) * 100
            if jd_skills else 0
        )

        return similarity_score, matched