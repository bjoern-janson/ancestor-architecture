class RewardTracker:
    """
    Tracks reward evolution.

    Useful for observing:

    - increasing agency
    - decreasing dependency
    - long-term alignment
    """


    def __init__(self):

        self.history = []



    def record(
        self,
        reward_components,
    ):

        self.history.append(
            reward_components
        )



    def latest(self):

        if not self.history:

            return None

        return self.history[-1]



    def average(
        self,
        key,
    ):

        if not self.history:

            return 0


        values = [
            item[key]
            for item in self.history
            if key in item
        ]


        if not values:

            return 0


        return sum(values) / len(values)
