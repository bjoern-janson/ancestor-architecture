from .base_agent import BaseAgent


class OracleAgent(BaseAgent):
    """
    Pure substitution baseline.

    Objective:
        maximize immediate task completion.

    Hypothesis:
        high assisted performance,
        low capability transfer.
    """

    def act(self, task):
        solution = self.solve(task)

        return {
            "answer": solution,
            "explanation": None,
            "assistance_level": 1.0,
        }

    def solve(self, task):
        """
        Placeholder for direct solution engine.
        """

        return f"complete_solution_for:{task}"
