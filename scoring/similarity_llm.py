import json

class LLMSimilarityScorer:
    """
    Uses a real LLM to evaluate semantic fit between JD and Resume.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def score(self, job_description, resume_text):
        prompt = self._build_prompt(job_description, resume_text)
        response = self.llm.generate(prompt)

        try:
            result = json.loads(response)
            return result
        except Exception:
            return {
                "score": 0,
                "reason": "Unable to parse LLM similarity output",
                "raw_output": response
            }

    def _build_prompt(self, jd, resume):
        return f"""
You are an expert technical recruiter.

Evaluate how well the RESUME fits the JOB DESCRIPTION semantically.
Consider transferable skills and domain overlap.

Job Description:
\"\"\"{jd}\"\"\"

Resume:
\"\"\"{resume}\"\"\"

Return ONLY valid JSON:
{{
  "score": <integer between 0 and 100>,
  "reason": "<short explanation>"
}}

Scoring guide:
- 0–20: Unrelated domains
- 21–40: Weak overlap
- 41–60: Partial but reasonable fit
- 61–80: Strong fit
- 81–100: Excellent fit
"""