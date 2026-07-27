class DependencyPenalty:
    """
    Detects substitution.

    A good AI should reduce
    future assistance requirement.
    """


    def calculate(
        self,
        assistance_frequency,
        independent_capability,
    ):

        if independent_capability == 0:

            return float("inf")


        return (
            assistance_frequency
            /
            independent_capability
        )



    def assistance_decay(
        self,
        previous_assistance,
        current_assistance,
    ):

        """
        Measures whether scaffolding
        is successfully fading.
        """

        return (
            previous_assistance
            -
            current_assistance
        )
