"""
src/experiments/registry.py

Central registry for all experiments.

The registry decouples experiment names from their implementations,
allowing new experiments to be added without modifying the runner.
"""

from typing import Dict, Type

from .agency_transfer_test import AgencyTransferExperiment
from .permeability_phase_transition import (
    PermeabilityPhaseTransitionExperiment,
)
from .baseline_comparisons import (
    BaselineComparisonExperiment,
)


EXPERIMENT_REGISTRY: Dict[str, Type] = {

    "agency_transfer":
        AgencyTransferExperiment,

    "permeability_transition":
        PermeabilityPhaseTransitionExperiment,

    "baseline_comparison":
        BaselineComparisonExperiment,

}


def available_experiments():

    """
    Returns a sorted list of registered experiments.
    """

    return sorted(
        EXPERIMENT_REGISTRY.keys()
    )


def get_experiment(name):

    """
    Returns the experiment class associated with a name.

    Raises
    ------
    ValueError
        If the experiment has not been registered.
    """

    if name not in EXPERIMENT_REGISTRY:

        available = ", ".join(
            available_experiments()
        )

        raise ValueError(
            f"Unknown experiment '{name}'. "
            f"Available experiments: {available}"
        )

    return EXPERIMENT_REGISTRY[name]


def create_experiment(
    name,
    config,
):

    """
    Factory function.

    Parameters
    ----------
    name : str
        Registered experiment name.

    config : ConfigLoader
        Loaded experiment configuration.

    Returns
    -------
    Experiment
        Instantiated experiment.
    """

    experiment_cls = get_experiment(
        name
    )

    return experiment_cls(
        config
    )


def register_experiment(
    name,
    experiment_cls,
):

    """
    Dynamically register a new experiment.

    Useful for external plugins or future extensions.
    """

    if name in EXPERIMENT_REGISTRY:

        raise ValueError(
            f"Experiment '{name}' "
            "is already registered."
        )

    EXPERIMENT_REGISTRY[name] = (
        experiment_cls
    )
