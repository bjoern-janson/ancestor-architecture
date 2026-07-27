class EvaluationLoop:
    """
    Evaluates whether capability survives
    removal of the AI.

    Implements:

    Remove oracle.
    Present novel problem.
    Measure retained capability.
    """


    def __init__(
        self,
        environment,
    ):

        self.environment = environment



    def evaluate(
        self,
        agent,
        episodes=50,
    ):

        scores = []


        for _ in range(episodes):

            task = (
                self.environment
                .generate_transfer_task()
            )


            action = (
                agent
                .act_without_assistance(
                    task
                )
            )


            result = (
                self.environment
                .step(action)
            )


            scores.append(
                result.get(
                    "score",
                    0,
                )
            )


        return {
            "independent_capability":
                sum(scores)
                /
                len(scores),

            "episodes":
                episodes,
        }
