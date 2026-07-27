from src.rewards import (
    AncestorReward,
    DependencyPenalty,
)


def test_ancestor_reward():

    reward = AncestorReward(
        alpha=1,
        beta=1,
        gamma=1,
    )


    value = reward.calculate(
        task_reward=10,
        human_agency_delta=5,
        future_agency_delta=2,
        dependency=3,
    )


    assert value == 14



def test_dependency_penalty():

    penalty = DependencyPenalty()


    value = penalty.calculate(
        assistance_frequency=10,
        independent_capability=5,
    )


    assert value == 2
