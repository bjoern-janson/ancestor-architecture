class UpdateEngine:
    """
    Controls model revision.

    Implements:

    failure
        ->
    information
        ->
    update
        ->
    improved model
    """


    def __init__(
        self,
        learning_rate=0.1,
    ):

        self.learning_rate = learning_rate

        self.updates = 0



    def calculate_revision_pressure(
        self,
        prediction_error,
    ):

        return (
            prediction_error
            *
            self.learning_rate
        )



    def update(
        self,
        model,
        belief_key,
        feedback,
    ):

        """
        Applies environmental feedback.
        """

        error = (
            0
            if feedback
            else 1
        )

        pressure = self.calculate_revision_pressure(
            error
        )


        if pressure > 0:

            model.revise(
                belief_key,
                success=False,
            )

            self.updates += 1

        else:

            model.revise(
                belief_key,
                success=True,
            )



    def update_velocity(
        self,
        time_elapsed,
    ):

        if time_elapsed == 0:
            return 0

        return (
            self.updates
            /
            time_elapsed
        )
