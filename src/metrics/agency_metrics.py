def agency_delta(
    capability_before,
    capability_after,
):
    """
    Measures human capability growth.

    ΔA = A_after - A_before
    """

    return capability_after - capability_before



def agency_roi(
    agency_gain,
    intervention_cost,
):
    """
    Capability generated per unit AI intervention.

    ROI_A =
        ΔA / intervention
    """

    if intervention_cost == 0:
        return float("inf")

    return agency_gain / intervention_cost



def capability_transfer(
    assisted_score,
    independent_score,
):
    """
    Measures whether assisted performance
    transfers into independent ability.
    """

    if assisted_score == 0:
        return 0

    return independent_score / assisted_score
