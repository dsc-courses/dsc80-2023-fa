"""
Imports and helper functions that we use in DSC 80.

Usage:

from dsc80_utils import *
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_inline.backend_inline import set_matplotlib_formats
from IPython.display import display, IFrame, HTML

# import plotly
# import plotly.figure_factory as ff
# import plotly.graph_objects as go
# import plotly.express as px
# from plotly.subplots import make_subplots
# import plotly.io as pio

# DSC 80 preferred styles
# pio.templates["dsc80"] = go.layout.Template(
#     layout=dict(
#         margin=dict(l=30, r=30, t=30, b=30),
#         autosize=True,
#         width=600,
#         height=400,
#         xaxis=dict(showgrid=True),
#         yaxis=dict(showgrid=True),
#         title=dict(x=0.5, xanchor="center"),
#     )
# )
# pio.templates.default = "simple_white+dsc80"

set_matplotlib_formats("svg")
sns.set_context("poster")
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# display options for numpy and pandas
np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

# Use plotly as default plotting engine
# pd.options.plotting.backend = "plotly"


def display_df(
    df, rows=pd.options.display.max_rows, cols=pd.options.display.max_columns
):
    """Displays n rows and cols from df"""
    with pd.option_context(
        "display.max_rows", rows, "display.max_columns", cols
    ):
        display(df)


def dfs_side_by_side(*dfs):
    """
    Displays two or more dataframes side by side.
    """
    display(
        HTML(
            f"""
        <div style="display: flex; gap: 1rem;">
        {''.join(df.to_html() for df in dfs)}
        </div>
    """
        )
    )


def permutation_test(data, col, group_col, test_statistic, N=1000):
    """
    Conduct a permutation test to compare two groups based on a given test
    statistic.

    This function computes the observed test statistic for the two groups in the
    dataset, and then generates a distribution of permuted test statistics by
    repeatedly shuffling the group labels and calculating the test statistic on
    the shuffled data. The result is a distribution of permuted statistics and
    the observed statistic for comparison.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame containing the data to be tested, along with the
        group labels.
    col : str
        The name of the column in `data` that contains the data values to be
        compared between the two groups.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.
    test_statistic : function
        A function that calculates the test statistic based on the data column
        and the group column. This function must accept three arguments: the
        data DataFrame, the name of the data column, and the name of the group
        column.
    N : int, optional (default=1000)
        The number of permutations to perform in the test.

    Returns
    -------
    shuffled_stats : np.ndarray
        An array of test statistics computed from the permuted datasets.
    obs : np.floating
        The observed test statistic calculated from the original data.

    Example
    -------
    >>> import numpy as np
    >>> import pandas as pd
    >>> def mean_diff(data, col, group_col):
    ...     group_means = data.groupby(group_col)[col].mean()
    ...     return np.abs(group_means.iloc[0] - group_means.iloc[1])
    >>> data = pd.DataFrame({
    ...     'value': [1, 2, 3, 4, 5, 6],
    ...     'group': ['A', 'A', 'A', 'B', 'B', 'B']
    ... })
    >>> perm_stats, obs_stat = permutation_test(data, 'value', 'group', mean_diff)
    """
    obs = test_statistic(data, col, group_col)
    shuffled = data.copy()

    shuffled_stats = []
    for _ in range(N):
        shuffled[col] = np.random.permutation(shuffled[col])
        shuffled_stat = test_statistic(shuffled, col, group_col)
        shuffled_stats.append(shuffled_stat)

    shuffled_stats = np.array(shuffled_stats)

    return shuffled_stats, obs


def diff_in_means(data, col, group_col):
    """
    Compute the difference in means between two groups.

    This function calculates the difference in means of the values in the
    specified column between two groups defined by the group column.

    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame containing the data and group labels.
    col : str
        The name of the column in `data` that contains the numeric data for
        which the mean will be computed.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.

    Returns
    -------
    float
        The difference in means between the two groups. The result is
        calculated as mean(group2) - mean(group1), where the group ordering is
        based on their appearance in the DataFrame.

    Example
    -------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'value': [1, 2, 3, 4, 5, 6],
    ...     'group': ['A', 'A', 'A', 'B', 'B', 'B']
    ... })
    >>> diff_in_means(data, 'value', 'group')
    np.float64(3.0)
    """
    return data.groupby(group_col)[col].mean().diff().iloc[-1]


def tvd(data, col, group_col):
    """
    Compute the Total Variation Distance (TVD) between two categorical
    distributions.

    The Total Variation Distance (TVD) measures the difference between the
    distributions of a categorical variable across two groups. It is defined as
    half the sum of the absolute differences between the group-wise proportions
    for each category.

    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame containing the data and group labels.
    col : str
        The name of the column in `data` that contains the categorical data.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.

    Returns
    -------
    float
        The Total Variation Distance (TVD) between the two distributions. A
        value of 0 indicates that the distributions are identical, while a value
        of 1 indicates that they are completely disjoint.

    Example
    -------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'category': ['X', 'X', 'Y', 'Y', 'Z', 'Z'],
    ...     'group': ['A', 'A', 'B', 'B', 'B', 'A']
    ... })
    >>> tvd(data, 'category', 'group')
    np.float64(0.6666666666666666)
    """

    tvd = (
        data.pivot_table(
            index=col, columns=group_col, aggfunc="size", fill_value=0
        )
        .apply(lambda x: x / x.sum())
        .diff(axis=1)
        .iloc[:, -1]
        .abs()
        .sum()
        / 2
    )

    return tvd


def ks(data, col, group_col):
    """
    Compute the Kolmogorov-Smirnov (KS) statistic between two distributions.

    The Kolmogorov-Smirnov (KS) statistic is used to measure the distance
    between the empirical distribution functions of two samples. This function
    applies the KS test to compare the distributions of a numeric column between
    two groups.

    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame containing the data and group labels.
    col : str
        The name of the column in `data` that contains the numeric data to
        compare.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.

    Returns
    -------
    float
        The Kolmogorov-Smirnov (KS) statistic, which measures the maximum
        distance between the two empirical cumulative distribution functions. A
        higher value indicates greater dissimilarity between the distributions.

    Example
    -------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'value': [1, 2, 3, 4, 5, 6],
    ...     'group': ['A', 'A', 'A', 'B', 'B', 'B']
    ... })
    >>> ks(data, 'value', 'group')
    np.float64(0.6666666666666666)
    """

    from scipy.stats import ks_2samp

    # should have only two values in column
    valA, valB = data[group_col].unique()
    ks, _ = ks_2samp(
        data.loc[data[group_col] == valA, col],
        data.loc[data[group_col] == valB, col],
    )

    return ks
