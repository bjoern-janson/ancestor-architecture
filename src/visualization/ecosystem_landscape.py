import matplotlib.pyplot as plt



def plot_ecosystem_space(
    capability,
    diversity,
    sovereignty,
    exploration,
):

    """
    Visualizes:

        A_net =
        C × D × S × E

    as an ecosystem fitness landscape.
    """


    agency = (
        capability
        *
        diversity
        *
        sovereignty
        *
        exploration
    )


    fig = plt.figure()

    ax = fig.add_subplot(
        111,
        projection="3d",
    )


    ax.scatter(
        capability,
        diversity,
        sovereignty,
        s=agency * 100,
    )


    ax.set_xlabel(
        "Capability"
    )

    ax.set_ylabel(
        "Diversity"
    )

    ax.set_zlabel(
        "Sovereignty"
    )


    return fig
