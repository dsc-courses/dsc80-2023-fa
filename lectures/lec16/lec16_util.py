import pandas as pd
import numpy as np

TEMPLATE = "seaborn"

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


def fit_polys(train_sample, degs):
    # Create all three Pipelines.
    pls = [
        Pipeline(
            [("poly", PolynomialFeatures(d)), ("lin-reg", LinearRegression())]
        )
        for d in degs
    ]

    # Fit all three Pipelines.
    [pl.fit(train_sample[["x"]], train_sample["y"]) for pl in pls]

    # Return the relevant fit Pipelines.
    return pls


def train_and_plot(train_sample, test_sample, degs):
    pred_funcs = fit_polys(train_sample, degs)

    rmses = [
        np.sqrt(
            np.mean(
                (pred_funcs[i].predict(test_sample[["x"]]) - test_sample["y"])
                ** 2
            )
        )
        for i in range(len(pred_funcs))
    ]
    titles = [
        f"Degree {degs[i]}, RMSE: {np.round(rmses[i], 3)}"
        for i in range(len(pred_funcs))
    ]

    fig = make_subplots(rows=1, cols=len(pred_funcs), subplot_titles=titles)

    for i in range(len(pred_funcs)):
        fig.add_trace(
            go.Scatter(
                x=test_sample["x"],
                y=test_sample["y"],
                name="Actual Data",
                mode="markers",
                marker={"color": "#4c72b0"},
            ),
            row=1,
            col=i + 1,
        )

        fig.add_trace(
            go.Scatter(
                x=test_sample["x"],
                y=pred_funcs[i].predict(test_sample[["x"]]),
                name="Predictions",
                line={"color": "orange", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

    fig.update_layout(template=TEMPLATE)

    fig["data"][0]["name"] = "Original Data"
    fig["data"][1]["name"] = "Fit Model"

    for i in range(2, len(fig["data"])):
        fig["data"][i]["showlegend"] = False

    return fig


def plot_multiple_models(sample_1, sample_2, degs):
    sample_1_funcs = fit_polys(sample_1, degs)
    sample_2_funcs = fit_polys(sample_2, degs)

    fig = make_subplots(
        rows=1,
        cols=len(degs),
        subplot_titles=[f"Degree {deg}" for deg in degs],
    )

    for i in range(len(degs)):
        fig.add_trace(
            go.Scatter(
                x=sample_1["x"],
                y=sample_1_funcs[i].predict(sample_1[["x"]]),
                line={"color": "orange", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

        fig.add_trace(
            go.Scatter(
                x=sample_2["x"],
                y=sample_2_funcs[i].predict(sample_2[["x"]]),
                line={"color": "purple", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

    fig.update_layout(template=TEMPLATE)

    for i in range(2):
        fig["data"][i]["name"] = f"Trained on Sample {i+1}"

    for i in range(2, len(fig["data"])):
        fig["data"][i]["showlegend"] = False

    return fig
