from .plots import create_plot



def plot_agency_transfer(
    results,
):

    """
    Visualizes:

    assisted capability
    versus
    retained independent capability
    """


    assisted = [
        r["assisted_performance"]
        for r in results
    ]


    independent = [
        r["independent_performance"]
        for r in results
    ]


    fig, ax = create_plot(
        title="Agency Transfer",
        xlabel="Training Episodes",
        ylabel="Capability",
    )


    ax.plot(
        assisted,
        label="AI assisted",
    )


    ax.plot(
        independent,
        label="Independent",
    )


    ax.legend()


    return fig
