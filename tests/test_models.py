from src.models import (
    CognitiveModel,
    BeliefState,
    UpdateEngine,
)


def test_belief_revision():

    belief = BeliefState(
        representation="model",
        confidence=0.5,
    )

    belief.weaken()

    assert belief.confidence < 0.5
    assert belief.failures_absorbed == 1



def test_model_update():

    model = CognitiveModel()

    model.add_belief(
        "test",
        lambda x: x,
        confidence=0.5,
    )

    model.revise(
        "test",
        success=False,
    )

    assert (
        model.beliefs["test"]
        .confidence
        < 0.5
    )



def test_update_velocity():

    engine = UpdateEngine()

    engine.updates = 10

    assert (
        engine.update_velocity(5)
        == 2
    )
