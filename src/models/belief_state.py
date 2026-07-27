from dataclasses import dataclass


@dataclass
class BeliefState:
    """
    Represents a single internal model claim.

    A belief is not treated as truth.
    It is treated as a temporary compression
    of reality.
    """

    representation: object

    confidence: float = 0.5

    evidence_count: int = 0

    failures_absorbed: int = 0


    def reinforce(self):

        self.confidence = min(
            1.0,
            self.confidence + 0.05
        )

        self.evidence_count += 1



    def weaken(self):

        self.confidence = max(
            0.0,
            self.confidence - 0.1
        )

        self.failures_absorbed += 1
