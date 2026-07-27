from .base_environment import BaseEnvironment


class EcosystemEnvironment(BaseEnvironment):
    """
    Multi-agent environment.

    Tests:

    C = capability
    D = diversity
    S = sovereignty
    E = exploration

    A_net = C * D * S * E
    """

    def __init__(self):

        super().__init__()

        self.agents = []


    def add_agent(self, agent):

        self.agents.append(agent)


    def generate_task(self):

        return {
            "environment_state": self.time,
            "novelty": self.calculate_novelty(),
        }


    def evaluate(self, actions):

        return {
            "ecosystem_score":
                self.calculate_ecosystem_agency(actions)
        }


    def calculate_novelty(self):

        return min(1.0, self.time / 100)


    def calculate_ecosystem_agency(
        self,
        actions
    ):

        capability = self.measure_capability(actions)
        diversity = self.measure_diversity(actions)
        sovereignty = self.measure_sovereignty(actions)
        exploration = self.measure_exploration(actions)

        return (
            capability
            * diversity
            * sovereignty
            * exploration
        )


    def measure_capability(self, actions):

        return min(1.0, len(actions) / 10)


    def measure_diversity(self, actions):

        strategies = set(
            str(a.get("type"))
            for a in actions
        )

        return min(1.0, len(strategies) / 5)


    def measure_sovereignty(self, actions):

        independent = sum(
            1 for a in actions
            if a.get("independent")
        )

        if len(actions) == 0:
            return 0

        return independent / len(actions)


    def measure_exploration(self, actions):

        novelty = sum(
            1 for a in actions
            if a.get("novel")
        )

        if len(actions) == 0:
            return 0

        return novelty / len(actions)
