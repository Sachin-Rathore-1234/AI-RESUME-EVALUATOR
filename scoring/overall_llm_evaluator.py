import json

class OverallLLMEvaluator:
    """
    Uses a real LLM (Groq) to make a holistic hiring decision
    based on all computed signals.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def evaluate(self, ctx):
        prompt = self._build_prompt(ctx)
        response = self.llm.generate(prompt)

        try:
            return json.loads(response)
        except Exception:
            return {
                "tier": "Tier B",
                "decision": "Manual review required",
                "reason": "LLM output could not be parsed as JSON",
                "raw_output": response
            }

    def _build_prompt(self, ctx):
        return f"""
You are a senior hiring manager making a FINAL hiring decision.

Job Summary:
{ctx["job_summary"]}

Candidate Evaluation Signals:

Similarity Score: {ctx["similarity_score"]}/100
Explanation: {ctx["similarity_explanation"]}

Achievement Score: {ctx["achievement_score"]}/100
Explanation: {ctx["achievement_explanation"]}

Ownership Score: {ctx["ownership_score"]}/100
Explanation: {ctx["ownership_explanation"]}

Instructions:
- Low similarity does NOT automatically mean rejection.
- Focus on impact, ownership, and potential.
- Be conservative and realistic.

Return ONLY valid JSON in this format:
{{
  "tier": "Tier A | Tier B | Tier C",
  "decision": "<short hiring action>",
  "reason": "<clear explanation>"
}}
"""