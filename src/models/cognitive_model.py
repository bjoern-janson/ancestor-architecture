from .belief_state import BeliefState


class CognitiveModel:
    """
    Internal representation system.

    Stores:
        - compressed representations
        - assumptions
        - confidence
        - revision history
    """


    def __init__(self):

        self.beliefs = {}

        self.revision_history = []



    def add_belief(
        self,
        key,
        representation,
        confidence=0.5,
    ):

        self.beliefs[key] = BeliefState(
            representation=representation,
            confidence=confidence,
        )



    def predict(
        self,
        key,
        input_data,
    ):

        belief = self.beliefs.get(key)

        if belief is None:
            return None

        return self.apply_representation(
            belief.representation,
            input_data,
        )



    def apply_representation(
        self,
        representation,
        input_data,
    ):

        """
        Placeholder representation engine.
        """

        return representation(input_data)



    def revise(
        self,
        key,
        success,
    ):

        belief = self.beliefs[key]


        if success:
            belief.reinforce()

        else:
            belief.weaken()


        self.revision_history.append(
            {
                "belief": key,
                "success": success,
            }
        )
