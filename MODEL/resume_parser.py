import json
from models.schema import ResumeData


class ResumeParser:
    """
    Mocked Resume Parser.
    In production, this will be backed by an open-source LLM (Mistral / LLaMA).
    """

    def parse(self, resume_text: str) -> ResumeData:
        # Simulated LLM output (realistic)
        parsed = {
            "skills": ["Python", "Kafka", "AWS", "Docker"],
            "experience": [
                {
                    "company": "XYZ",
                    "role": "Backend Engineer",
                    "duration_months": 24,
                    "projects": [
                        {
                            "description": "Built Kafka-based data pipeline",
                            "tools": ["Kafka", "Python", "AWS"],
                            "metrics": ["Handled 1M events/day", "Reduced latency by 40%"]
                        }
                    ]
                }
            ],
            "achievements": [
                "Reduced API latency by 40%",
                "Processed 1M events/day"
            ]
        }

        return ResumeData(**parsed)