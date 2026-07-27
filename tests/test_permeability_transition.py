from src.models import UpdateEngine



def test_revision_occurs_under_failure():

    engine = UpdateEngine(
        learning_rate=0.5
    )


    pressure = (
        engine
        .calculate_revision_pressure(
            prediction_error=1
        )
    )


    assert pressure > 0



def test_no_revision_without_error():

    engine = UpdateEngine(
        learning_rate=0.5
    )


    pressure = (
        engine
        .calculate_revision_pressure(
            prediction_error=0
        )
    )


    assert pressure == 0
