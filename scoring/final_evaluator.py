class FinalEvaluator:
    """
    Aggregates multiple scores into a final score and hiring tier.
    """

    def __init__(
        self,
        similarity_weight=0.4,
        achievement_weight=0.35,
        ownership_weight=0.25
    ):
        self.sim_w = similarity_weight
        self.ach_w = achievement_weight
        self.own_w = ownership_weight

    def evaluate(self, similarity, achievement, ownership):
        """
        Inputs are expected in range 0–100
        """

        final_score = (
            self.sim_w * similarity +
            self.ach_w * achievement +
            self.own_w * ownership
        )

        tier = self._assign_tier(final_score)

        explanation = {
            "similarity_contribution": round(self.sim_w * similarity, 2),
            "achievement_contribution": round(self.ach_w * achievement, 2),
            "ownership_contribution": round(self.own_w * ownership, 2)
        }

        return round(final_score, 2), tier, explanation

    def _assign_tier(self, score):
        if score >= 75:
            return "Tier A (Fast-track)"
        elif score >= 50:
            return "Tier B (Technical Screen)"
        else:
            return "Tier C (Needs Evaluation)"