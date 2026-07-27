from .plots import create_plot



def plot_permeability_transition(
    results,
):

    """
    Visualizes:

        κ_c phase transition

    x:
        constraint-consequence coupling

    y:
        model permeability
    """


    kappas = [
        item["kappa"]
        for item in results
    ]


    permeability = [
        item["permeability"]
        for item in results
    ]


    fig, ax = create_plot(
        title="Permeability Phase Transition",
        xlabel="Constraint-Consequence Coupling (κ)",
        ylabel="Model Permeability",
    )


    ax.plot(
        kappas,
        permeability,
        marker="o",
    )


    return fig
