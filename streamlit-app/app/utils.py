import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_barplot(
    data: pd.DataFrame, x: str, y: str, hue: str, xlabel: str, suptitle: str
) -> tuple:
    """
    Create a bar plot using seaborn and matplotlib.

    Parameters:
    - data (pd.DataFrame): The data to plot.
    - x (str): The name of the column in `data` to be used for the x-axis.
    - y (str): The name of the column in `data` to be used for the y-axis.
    - hue (str): The name of the column in `data` to be used for color encoding.
    - xlabel (str): The label for the x-axis.
    - suptitle (str): The overall title for the figure.

    Returns:
    - fig (matplotlib.figure.Figure): The created figure.
    - ax (matplotlib.axes._axes.Axes): The created axes.
    """
    fig, ax = plt.subplots()
    sns.set_theme(style="ticks")
    sns.barplot(data=data, x=x, y=y, hue=hue, ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("")
    ax.set_title("")
    ax.legend().remove()
    fig.suptitle(suptitle)
    fig.tight_layout()
    return (fig, ax)


def plot_boxplot(
    data: pd.DataFrame, x: str, hue: str, gap: float, leg_loc: str, suptitle: str
) -> tuple:
    """
    Creates a boxplot using the seaborn library and customizes the plot.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to be plotted.
    x (str): The name of the column to be used for the x-axis.
    hue (str): The name of the column to be used for grouping the data by color.
    gap (float): The amount of space between the boxes.
    leg_loc (str): The location for the legend on the plot.
    suptitle (str): The overall title for the figure.

    Returns:
    tuple: A tuple containing the matplotlib Figure and Axes objects of the plot.
    """
    fig, ax = plt.subplots()
    sns.set_theme(style="ticks")
    sns.boxplot(
        data=data,
        x=x,
        hue=hue,
        gap=gap,
        ax=ax,
    )
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("")
    sns.move_legend(ax, leg_loc)
    fig.suptitle(suptitle)
    fig.tight_layout()
    return (fig, ax)
