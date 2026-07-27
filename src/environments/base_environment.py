from abc import ABC, abstractmethod


class BaseEnvironment(ABC):
    """
    Abstract environment.

    Environment provides:
        - tasks
        - feedback
        - consequences
        - evaluation
    """

    def __init__(self):
        self.time = 0
        self.history = []

    @abstractmethod
    def generate_task(self):
        pass

    @abstractmethod
    def evaluate(self, action):
        pass

    def step(self, action):

        result = self.evaluate(action)

        self.history.append(
            {
                "time": self.time,
                "action": action,
                "result": result,
            }
        )

        self.time += 1

        return result
