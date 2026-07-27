def ecosystem_agency(
    capability,
    diversity,
    sovereignty,
    exploration,
):
    """
    A_net = C × D × S × E
    """

    return (
        capability
        *
        diversity
        *
        sovereignty
        *
        exploration
    )



def diversity_score(strategies):
    """
    Measures number of distinct approaches.
    """

    if len(strategies) == 0:
        return 0

    return len(set(strategies)) / len(strategies)



def sovereignty_score(
    independent_actions,
    total_actions,
):
    """
    Measures self-directed action.
    """

    if total_actions == 0:
        return 0

    return independent_actions / total_actions



def exploration_score(
    novel_discoveries,
    total_attempts,
):
    """
    Measures creation of new solution space.
    """

    if total_attempts == 0:
        return 0

    return novel_discoveries / total_attempts
