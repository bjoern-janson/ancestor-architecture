from .base_trainer import BaseTrainer


class AncestorTrainer(BaseTrainer):
    """
    Training loop optimized around:

    R_ancestor =
        R_task
        + αΔA_human
        + γΔA_future
        - βD_dependency
    """


    def __init__(
        self,
        agent,
        environment,
        reward_function,
    ):

        super().__init__(
            agent,
            environment,
        )

        self.reward_function = reward_function



    def train_step(self):

        task = (
            self.environment
            .generate_task()
        )


        action = (
            self.agent
            .act(task)
        )


        result = (
            self.environment
            .step(action)
        )


        reward = (
            self.reward_function
            .calculate(
                task_reward=result.get(
                    "task_reward",
                    0,
                ),

                human_agency_delta=result.get(
                    "agency_delta",
                    0,
                ),

                future_agency_delta=result.get(
                    "future_agency_delta",
                    0,
                ),

                dependency=result.get(
                    "dependency",
                    0,
                ),
            )
        )


        self.agent.update(
            reward
        )


        record = {
            **result,
            "ancestor_reward": reward,
        }


        self.history.append(record)


        return record
