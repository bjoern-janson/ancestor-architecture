import random


def set_seed(seed=42):

    """
    Makes experiments reproducible.
    """

    random.seed(seed)

    try:
        import numpy as np

        np.random.seed(seed)

    except ImportError:
        pass
