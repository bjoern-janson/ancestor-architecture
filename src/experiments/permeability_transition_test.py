from ..metrics.epistemic_metrics import (
    model_permeability,
)


def run_permeability_test(
    agent_factory,
    environment_factory,
    coupling_values,
):
    """
    Tests:

    κ > κ_c ?

    Does stronger
    constraint-consequence coupling
    produce recursive adaptation?
    """

    results = []


    for kappa in coupling_values:

        environment = environment_factory(
            coupling=kappa
        )

        agent = agent_factory()


        failures = 0
        revisions = 0


        for _ in range(100):

            task = environment.generate_task()

            action = agent.act(task)

            feedback = environment.step(
                action
            )


            if feedback.get(
                "error_signal",
                False
            ):
                failures += 1

                agent.update_model()

                revisions += 1


        permeability = model_permeability(
            failures,
            max(1, revisions),
        )


        results.append(
            {
                "kappa": kappa,
                "permeability": permeability,
            }
        )


    return results
