class AncestorReward:
    """
    Full ancestor objective.

    Optimizes:
        task success
        human capability growth
        future capability propagation

    Penalizes:
        dependency creation
    """


    def __init__(
        self,
        alpha=1.0,
        beta=1.0,
        gamma=1.0,
    ):

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma



    def calculate(
        self,
        task_reward,
        human_agency_delta,
        future_agency_delta,
        dependency,
    ):

        return (
            task_reward
            +
            self.alpha * human_agency_delta
            +
            self.gamma * future_agency_delta
            -
            self.beta * dependency
        )



    def components(
        self,
        task_reward,
        human_agency_delta,
        future_agency_delta,
        dependency,
    ):

        return {
            "task_reward": task_reward,
            "agency_growth": human_agency_delta,
            "future_agency": future_agency_delta,
            "dependency_penalty": -dependency,
            "total":
                self.calculate(
                    task_reward,
                    human_agency_delta,
                    future_agency_delta,
                    dependency,
                )
        }
