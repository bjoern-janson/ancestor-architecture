class CompressionEvaluator:
    """
    Measures useful compression.

    Model quality:

        useful preserved structure
        ---------------------------
        complexity required
    """


    def __init__(
        self,
        useful_structure,
        complexity,
    ):

        self.useful_structure = useful_structure
        self.complexity = complexity



    def efficiency(self):

        if self.complexity == 0:

            return 0


        return (
            self.useful_structure
            /
            self.complexity
        )



    def compression_shadow(
        self,
        discarded_information,
    ):

        """
        Represents information lost
        during compression.
        """

        return discarded_information
