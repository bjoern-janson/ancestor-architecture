def agency_delta(before, after):
    """
    ΔA_human

    Positive means capability increased.
    """

    return after - before



def dependency_index(
    assistance_frequency,
    independent_performance,
):
    """
    Measures reliance.

    Higher = more dependency.
    """

    if independent_performance == 0:
        return float("inf")

    return assistance_frequency / independent_performance



def agency_roi(
    agency_gain,
    intervention_cost,
):
    """
    Capability generated per unit intervention.
    """

    if intervention_cost == 0:
        return float("inf")

    return agency_gain / intervention_cost



def ancestor_reward(
    task_reward,
    human_agency_delta,
    future_agency_delta,
    dependency_penalty,
    alpha=1,
    beta=1,
    gamma=1,
):

    return (
        task_reward
        + alpha * human_agency_delta
        + gamma * future_agency_delta
        - beta * dependency_penalty
    )
