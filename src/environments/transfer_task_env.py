from .base_environment import BaseEnvironment


class TransferTaskEnvironment(BaseEnvironment):
    """
    Measures whether AI interaction
    creates independent capability.

    Phase:

    1. assisted training
    2. AI removal
    3. novel task evaluation
    """

    def __init__(self):

        super().__init__()

        self.training_tasks = []
        self.test_tasks = []


    def generate_task(self):

        return {
            "type": "training",
            "difficulty": self.time + 1,
        }


    def generate_transfer_task(self):

        return {
            "type": "novel",
            "difficulty": self.time + 2,
        }


    def evaluate(self, action):

        return {
            "score": self.score(action),
            "transfer": True,
        }


    def score(self, action):

        if action.get("independent_reasoning"):
            return 1.0

        return 0.5
