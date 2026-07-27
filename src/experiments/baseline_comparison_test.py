from ..metrics.agency_metrics import (
    agency_delta,
)

from ..metrics.dependency_metrics import (
    dependency_index,
)



def evaluate_agent(
    agent,
    environment,
    episodes=50,
):

    performance = []
    assistance = []


    for _ in range(episodes):

        task = environment.generate_task()

        action = agent.act(task)

        result = environment.step(
            action
        )

        performance.append(
            result.get(
                "score",
                0
            )
        )

        assistance.append(
            action.get(
                "assistance_level",
                0
            )
        )


    return {
        "performance":
            sum(performance)
            /
            len(performance),

        "assistance":
            sum(assistance)
            /
            len(assistance),
    }



def run_baseline_comparison(
    agents,
    environment,
):

    results = {}


    for name, agent in agents.items():

        results[name] = evaluate_agent(
            agent,
            environment,
        )


    return results
