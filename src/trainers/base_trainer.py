class BaseTrainer:
    """
    Generic agent-environment training loop.
    """


    def __init__(
        self,
        agent,
        environment,
    ):

        self.agent = agent
        self.environment = environment

        self.history = []



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

        self.history.append(result)

        return result



    def train(
        self,
        episodes=100,
    ):

        for _ in range(episodes):

            self.train_step()


        return self.history
