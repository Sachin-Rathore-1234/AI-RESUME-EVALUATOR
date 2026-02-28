from utils.groq_llm import GroqLLMClient
from scoring.similarity_llm import LLMSimilarityScorer
from scoring.achievement_llm import LLMAchievementScorer
from scoring.overall_llm_evaluator import OverallLLMEvaluator

llm_client = GroqLLMClient()

job_description = """
Backend Engineer working on distributed data systems, streaming platforms,
and scalable backend services.
"""

resume_text = """
Built real-time data pipelines using AWS Kinesis.
Designed fault-tolerant backend services in Python.
"""

achievements_text = """
Designed a fault-tolerant data ingestion pipeline used across teams.
Reduced processing latency by improving system architecture.
"""

# 1️⃣ LLM Screening
similarity_scorer = LLMSimilarityScorer(llm_client)
similarity_result = similarity_scorer.score(job_description, resume_text)

# 2️⃣ LLM Achievement
achievement_scorer = LLMAchievementScorer(llm_client)
achievement_result = achievement_scorer.score(achievements_text)

# 3️⃣ Ownership (already LLM-based)
ownership_score = 72  # from previous ownership LLM

# 4️⃣ Final LLM decision
context = {
    "job_summary": "Backend engineer role focused on distributed systems",
    "similarity_score": similarity_result["score"],
    "similarity_explanation": similarity_result["reason"],
    "achievement_score": achievement_result["score"],
    "achievement_explanation": achievement_result["reason"],
    "ownership_score": ownership_score,
    "ownership_explanation": "Strong system ownership"
}

overall = OverallLLMEvaluator(llm_client)
final_decision = overall.evaluate(context)

print("\n--- LLM SCREENING ---")
print(similarity_result)

print("\n--- LLM ACHIEVEMENT ---")
print(achievement_result)

print("\n--- FINAL AI DECISION ---")
print(final_decision)