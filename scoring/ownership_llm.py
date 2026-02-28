import json


class LLNOwnershipScorer:
    """
    LLM-based ownership/depth scorer.
    Evaluates how much responsibility and leadership the candidate had.
    """

    def __init__(self, llm_client):
        """
        llm_client must expose:
        generate(prompt: str) -> str
        """
        self.llm = llm_client

    def score(self, experience_text):
        if not experience_text:
            return 0, "No experience description provided"

        prompt = self._build_prompt(experience_text)
        response = self.llm.generate(prompt)

        try:
            parsed = json.loads(response)
            score = int(parsed["score"])
            explanation = parsed["explanation"]
        except Exception:
            score = 50
            explanation = "Unable to reliably parse ownership evaluation"

        return min(max(score, 0), 100), explanation

    def _build_prompt(self, experience_text):
        return f"""
You are a senior engineering interviewer.

Evaluate the candidate's OWNERSHIP and DEPTH of responsibility.

Scoring rubric:
- 0–20: No ownership, only assisted or followed instructions
- 21–40: Partial contribution, limited responsibility
- 41–60: Owned individual components or features
- 61–80: Owned major systems or led design decisions
- 81–100: End-to-end ownership, architectural or team leadership

Experience Description:
\"\"\"{experience_text}\"\"\"

Return ONLY valid JSON in this format:
{{
  "score": <integer between 0 and 100>,
  "explanation": "<1–2 sentence justification>"
}}

Be conservative. Do not inflate scores.
"""