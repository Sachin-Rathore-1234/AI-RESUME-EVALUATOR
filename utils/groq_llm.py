from groq import Groq

class GroqLLMClient:
    """
    Real LLM client using Groq API (stable model).
    """

    def __init__(self, api_key=None):
        self.client = Groq(api_key=api_key)

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ STABLE MODEL
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior AI hiring decision system."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,  # deterministic
        )

        return completion.choices[0].message.content