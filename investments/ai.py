import random

class AIInvestmentAdvisor:
    def recommend(self, user):
        # Mock recommendation logic
        # Replace with actual AI/ML model
        recommendations = [
            {"name": "Tech Stock", "risk_level": "High", "expected_return": "15%"},
            {"name": "Government Bonds", "risk_level": "Low", "expected_return": "3%"},
        ]
        return random.choice(recommendations)
