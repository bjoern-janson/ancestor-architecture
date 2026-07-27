class Curriculum:
    """
    Controls environmental difficulty.

    A true ancestor system should
    gradually increase novelty,
    not permanently optimize inside
    a predictable environment.
    """


    def __init__(
        self,
        initial_difficulty=0.1,
        growth_rate=0.05,
    ):

        self.difficulty = initial_difficulty
        self.growth_rate = growth_rate



    def advance(self):

        self.difficulty += (
            self.growth_rate
        )


        return self.difficulty



    def current(self):

        return self.difficulty



    def generate_constraints(self):

        return {
            "novelty":
                self.difficulty,

            "uncertainty":
                self.difficulty,

            "feedback_delay":
                self.difficulty,
        }
