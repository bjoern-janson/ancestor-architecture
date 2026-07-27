import matplotlib.pyplot as plt



def create_plot(
    title,
    xlabel,
    ylabel,
):

    fig, ax = plt.subplots()

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return fig, ax
