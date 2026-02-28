class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return """
        {
          "score": 72,
          "explanation": "Candidate owned the design and implementation of core systems, indicating strong responsibility but limited leadership scope."
        }
        """