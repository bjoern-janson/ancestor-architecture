def dependency_index(
    assistance_frequency,
    independent_capability,
):
    """
    Measures reliance on external intelligence.

    Higher value =
        greater dependency risk.
    """

    if independent_capability == 0:
        return float("inf")

    return assistance_frequency / independent_capability



def assistance_ratio(
    ai_actions,
    total_actions,
):
    """
    Percentage of decisions requiring AI.
    """

    if total_actions == 0:
        return 0

    return ai_actions / total_actions



def substitution_score(
    assisted_performance,
    independent_performance,
):
    """
    Detects substitution.

    High assisted performance combined
    with low independent performance
    indicates oracle dependence.
    """

    return (
        assisted_performance
        -
        independent_performance
    )
