import time


class ExperimentLogger:
    """
    Lightweight experiment tracker.
    """

    def __init__(self, name):

        self.name = name

        self.start_time = time.time()

        self.records = []


    def log(self, data):

        self.records.append(
            {
                "timestamp": time.time(),
                **data,
            }
        )


    def summary(self):

        return {
            "experiment": self.name,
            "duration":
                time.time()
                -
                self.start_time,
            "records":
                len(self.records),
            "data":
                self.records,
        }
