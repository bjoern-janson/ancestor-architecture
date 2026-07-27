from .base_environment import BaseEnvironment


class ChangingRulesEnv(BaseEnvironment):
    """
    Tests permeability.

    The environment changes after agents
    become confident in their existing models.

    Goal:
        measure recovery after model failure.
    """

    def __init__(self, change_point=50):
        super().__init__()

        self.change_point = change_point

        self.rule_version = 0


    def generate_task(self):

        if self.time >= self.change_point:
            self.rule_version = 1

        return {
            "input": self.time,
            "rule_version": self.rule_version,
        }


    def evaluate(self, action):

        expected = self.solve(action["input"])

        success = action.get("answer") == expected

        return {
            "success": success,
            "rule_version": self.rule_version,
            "error_signal": not success,
        }


    def solve(self, value):

        if self.rule_version == 0:
            return value * 2

        return value * 3
