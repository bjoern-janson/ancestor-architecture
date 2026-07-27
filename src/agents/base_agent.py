from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self):
        self.history = []
        self.performance_log = []

    @abstractmethod
    def act(self, task):
        pass

    def observe_feedback(self, feedback):
        self.history.append(feedback)

    def update(self, feedback=None):
        """
        Update internal model based on feedback.
        """

        self.observe_feedback(feedback)

        self.update_model()

    def update_model(self):
        pass

    def record_performance(self, score):
        self.performance_log.append(score)
