import argparse


from src.agents import AncestorAgent
from src.environments import TransferTaskEnv

from src.rewards import AncestorReward

from src.trainers import (
    AncestorTrainer,
)

from src.visualization import (
    plot_agency_transfer,
    plot_permeability_transition,
)



def run_agency_transfer():

    print(
        "Running agency transfer experiment..."
    )


    agent = AncestorAgent()

    environment = TransferTaskEnv()


    reward = AncestorReward(
        alpha=1.0,
        beta=1.0,
        gamma=1.0,
    )


    trainer = AncestorTrainer(
        agent=agent,
        environment=environment,
        reward_function=reward,
    )


    history = trainer.train(
        episodes=100
    )


    results = []


    for item in history:

        results.append(
            {
                "assisted_performance":
                    item.get(
                        "task_reward",
                        item.get(
                            "score",
                            0,
                        ),
                    ),

                "independent_performance":
                    item.get(
                        "agency_delta",
                        0,
                    ),
            }
        )


    fig = plot_agency_transfer(
        results
    )


    fig.savefig(
        "agency_transfer.png",
        dpi=300,
        bbox_inches="tight",
    )


    print(
        "Saved agency_transfer.png"
    )


    print(
        "Agency transfer complete."
    )



def run_permeability_transition():

    print(
        "Running permeability phase transition..."
    )


    results = []


    for kappa in [
        i / 10
        for i in range(0, 21)
    ]:

        permeability = (
            kappa
            /
            (1 + kappa)
        )


        results.append(
            {
                "kappa":
                    kappa,

                "permeability":
                    permeability,
            }
        )


    fig = plot_permeability_transition(
        results
    )


    fig.savefig(
        "permeability_transition.png",
        dpi=300,
        bbox_inches="tight",
    )


    print(
        "Saved permeability_transition.png"
    )


    print(
        "Permeability transition complete."
    )



def main():

    parser = argparse.ArgumentParser(
        description=
        "Ancestor Architecture Research Framework"
    )


    parser.add_argument(
        "--experiment",
        required=True,
        choices=[
            "agency_transfer",
            "permeability_transition",
        ],
    )


    args = parser.parse_args()


    if args.experiment == "agency_transfer":

        run_agency_transfer()


    elif args.experiment == "permeability_transition":

        run_permeability_transition()



if __name__ == "__main__":

    main()
