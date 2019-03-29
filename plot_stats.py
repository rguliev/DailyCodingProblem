import pandas as pd
import matplotlib.pyplot as plt

def plot_hist(s, bins=None, stats_pos=None, stats0_pos=None):
    """
    Returns plt (matplotlib.pyplot) object with a histogram of pandas.Series s.
    Optionally stats <mean, median, min, max, and std> can be added to the plot.
    Both including and excluding zero values.
    """
    assert isinstance(s, pd.Series)
    
    if stats_pos is not None:
        stats  = s.agg(['mean', 'median', 'min', 'max', 'std'])
    if stats0_pos is not None:
        stats0 = s[s > 0].agg(['mean', 'median', 'min', 'max', 'std'])
    if bins is not None:
        s.hist(edgecolor='black',grid=False, bins=bins)
    else:
        s.hist(edgecolor='black',grid=False)
    plt.minorticks_on()
    plt.gca().yaxis.grid(True, linestyle='--', which='major')
    plt.gca().yaxis.grid(True, linestyle='--', which='minor', alpha=0.4)
    plt.ylabel('Count')
    if stats_pos is not None:
        plt.text(
            stats_pos[0], stats_pos[1],
            "mean = %(mean)0.1f\nmedian = %(median)0.1f\nmin = %(min)0.1f\nmax = %(max)0.1f" % stats,
            verticalalignment='top', horizontalalignment='left',
            fontsize=13)
    if stats0_pos is not None:
        plt.text(
            stats0_pos[0], stats0_pos[1],
        "Без учета 0\nmean = %(mean)0.1f\nmedian = %(median)0.1f\nmin = %(min)0.1f\nmax = %(max)0.1f" % stats0,
        verticalalignment='top', horizontalalignment='left',
        fontsize=13)
    return plt

def plot_value_counts(s, custom_labels=None, rot=0):
    """
    Returns plt (matplotlib.pyplot) object with a barplot (counts) of pandas.Series s.
    Optionally custom labels and labels rotation can be provided
    """
    assert isinstance(s, pd.Series)

    if custom_labels is not None:
        s = s.astype('category')
        s.cat.categories = custom_labels
    s.value_counts(sort=False).plot(kind='bar', rot=rot, grid=False)
    plt.gca().yaxis.grid(True, linestyle='--', which='major')
    plt.yticks(s.value_counts().tolist())
    plt.ylabel('Count')
    return plt