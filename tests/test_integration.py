from src.rewards import AncestorReward
from src.models import CognitiveModel


def test_ancestor_pipeline():

    model = CognitiveModel()


    model.add_belief(
        "world_model",
        lambda x: x,
    )


    reward = AncestorReward()


    score = reward.calculate(
        task_reward=10,
        human_agency_delta=5,
        future_agency_delta=5,
        dependency=0,
    )


    assert score > 0
    assert (
        "world_model"
        in model.beliefs
    )
