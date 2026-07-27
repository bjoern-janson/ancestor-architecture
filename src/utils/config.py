from dataclasses import dataclass, field


@dataclass
class ExperimentConfig:
    """
    Global experiment configuration.

    Designed around the ancestor framework:

    - adaptation
    - permeability
    - agency transfer
    - dependency reduction
    """

    seed: int = 42

    episodes: int = 100

    learning_rate: float = 0.01

    alpha_agency: float = 1.0
    beta_dependency: float = 1.0
    gamma_future: float = 1.0

    coupling_values: list = field(
        default_factory=lambda: [
            0.0,
            0.25,
            0.5,
            0.75,
            1.0,
        ]
    )

    def ancestor_objective(
        self,
        task_reward,
        agency_delta,
        future_agency_delta,
        dependency,
    ):
        """
        R_ancestor =
        R_task
        + αΔA_human
        + γΔA_future
        - βD_dependency
        """

        return (
            task_reward
            +
            self.alpha_agency * agency_delta
            +
            self.gamma_future * future_agency_delta
            -
            self.beta_dependency * dependency
        )
