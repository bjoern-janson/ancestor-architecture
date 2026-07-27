from .base_agent import BaseAgent


class TutorAgent(BaseAgent):
    """
    Educational scaffolding baseline.

    Objective:
        improve learning through explanation.
    """

    def act(self, task):

        return {
            "answer": None,
            "hint": self.generate_hint(task),
            "explanation": self.explain(task),
            "assistance_level": 0.6,
        }

    def generate_hint(self, task):
        return f"hint_for:{task}"

    def explain(self, task):
        return f"explanation_for:{task}"
