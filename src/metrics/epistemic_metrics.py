def update_velocity(
    model_change,
    time_elapsed,
):
    """
    Measures adaptation speed.

    V_u = ΔModel / Δt
    """

    if time_elapsed == 0:
        return 0

    return model_change / time_elapsed



def model_permeability(
    absorbed_failures,
    revision_resistance,
):
    """
    Measures ability to integrate failure.

    P_M =
        failure absorption /
        resistance to revision
    """

    if revision_resistance == 0:
        return float("inf")

    return absorbed_failures / revision_resistance



def compression_efficiency(
    useful_structure,
    complexity,
):
    """
    Measures useful compression.

    Model quality =
        preserved structure / complexity
    """

    if complexity == 0:
        return 0

    return useful_structure / complexity



def intelligence_index(
    model_quality,
    update_velocity,
    permeability,
):
    """
    Core epistemic equation.

    I ≈ M_q × V_u × P_M
    """

    return (
        model_quality
        *
        update_velocity
        *
        permeability
    )
