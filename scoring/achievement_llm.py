import json

class LLMAchievementScorer:
    """
    Uses a real LLM to judge impact and achievement quality.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def score(self, achievements_text):
        prompt = self._build_prompt(achievements_text)
        response = self.llm.generate(prompt)

        try:
            result = json.loads(response)
            return result
        except Exception:
            return {
                "score": 0,
                "reason": "Unable to parse LLM achievement output",
                "raw_output": response
            }

    def _build_prompt(self, achievements):
        return f"""
You are a senior engineering interviewer.

Evaluate the IMPACT of the following achievements.

Achievements:
\"\"\"{achievements}\"\"\"

Return ONLY valid JSON:
{{
  "score": <integer between 0 and 100>,
  "reason": "<short explanation>"
}}

Scoring guide:
- 0–20: No real impact
- 21–40: Task-level work
- 41–60: Solid individual contribution
- 61–80: High-impact, system-level work
- 81–100: Exceptional, org-wide impact
"""