from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Abstract agent architecture.

    All agents receive:
        - task
        - environment feedback
        - interaction history

    and produce:
        - response/action
        - internal update
    """

    def __init__(self):
        self.history = []
        self.performance_log = []

    @abstractmethod
    def act(self, task):
        pass

    def observe_feedback(self, feedback):
        """
        Process environmental consequences.
        """
        self.history.append(feedback)

    def update_model(self):
        """
        Optional self-revision mechanism.
        """
        pass

    def record_performance(self, score):
        self.performance_log.append(score)
