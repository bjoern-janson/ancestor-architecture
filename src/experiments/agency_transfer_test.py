from ..metrics.agency_metrics import (
    agency_delta,
    capability_transfer,
)

from ..metrics.dependency_metrics import (
    dependency_index,
)


def run_agency_transfer_test(
    agent,
    environment,
    training_steps=50,
):
    """
    Tests:

    Does AI assistance create
    independent human capability?

    Training:
        Human + AI

    Evaluation:
        Human alone
    """

    assisted_scores = []
    independent_scores = []

    for _ in range(training_steps):

        task = environment.generate_task()

        response = agent.act(task)

        result = environment.step(response)

        assisted_scores.append(
            result.get("score", 0)
        )


    for _ in range(training_steps):

        task = environment.generate_transfer_task()

        independent_action = {
            "independent_reasoning": True,
            "task": task,
        }

        result = environment.step(
            independent_action
        )

        independent_scores.append(
            result.get("score", 0)
        )


    assisted_average = (
        sum(assisted_scores)
        /
        len(assisted_scores)
    )

    independent_average = (
        sum(independent_scores)
        /
        len(independent_scores)
    )


    return {
        "assisted_performance": assisted_average,
        "independent_performance": independent_average,
        "transfer_ratio": capability_transfer(
            assisted_average,
            independent_average,
        ),
        "agency_gain": agency_delta(
            0,
            independent_average,
        ),
    }
