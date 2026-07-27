class AgencyReward:
    """
    Measures whether the system
    increases human capability.

    ΔA = A_after - A_before
    """


    def calculate(
        self,
        capability_before,
        capability_after,
    ):

        return (
            capability_after
            -
            capability_before
        )



    def transfer_reward(
        self,
        assisted_score,
        independent_score,
    ):

        """
        Rewards capability that remains
        after AI removal.
        """

        if assisted_score == 0:

            return 0


        return (
            independent_score
            /
            assisted_score
        )



    def lineage_reward(
        self,
        downstream_capability,
    ):

        """
        Measures whether the user
        can now increase others' agency.
        """

        return downstream_capability
