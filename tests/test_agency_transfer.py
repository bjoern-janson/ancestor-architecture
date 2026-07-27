from src.rewards import AgencyReward



def test_remove_oracle_condition():

    metric = AgencyReward()


    transfer = metric.transfer_reward(
        assisted_score=100,
        independent_score=80,
    )


    assert transfer == 0.8



def test_positive_agency_transfer():

    metric = AgencyReward()


    delta = metric.calculate(
        capability_before=10,
        capability_after=15,
    )


    assert delta > 0
