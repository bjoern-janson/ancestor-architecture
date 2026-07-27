from .base_agent import BaseAgent


class AncestorAgent(BaseAgent):
    """
    Experimental ancestor architecture.

    Objective:

    R =
        R_task
        + alpha * ΔA_human
        + gamma * ΔA_future
        - beta * D_dependency

    Core behaviors:

    - adaptive assistance
    - calibrated friction
    - capability transfer
    - reduced dependency
    """

    def __init__(
        self,
        alpha=1.0,
        beta=1.0,
        gamma=1.0,
    ):
        super().__init__()

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.user_capability_estimate = 0.0
        self.dependency_estimate = 0.0


    def act(self, task):

        assistance = self.choose_assistance(task)

        return {
            "response": assistance,
            "assistance_level": self.estimate_assistance(),
            "goal": "increase_future_capability",
        }


    def choose_assistance(self, task):

        capability = self.user_capability_estimate

        if capability < self.required_level(task):
            return self.provide_scaffold(task)

        return self.provide_challenge(task)


    def provide_scaffold(self, task):

        return {
            "type": "scaffold",
            "content": f"framework_for:{task}"
        }


    def provide_challenge(self, task):

        return {
            "type": "challenge",
            "content": f"question_for:{task}"
        }


    def required_level(self, task):

        return 0.5


    def estimate_assistance(self):

        return self.dependency_estimate
