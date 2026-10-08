"""Explore synthetic measurements with the COSMOS project environment."""

import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    from project.main import mean_measurement
    return mean_measurement, mo, np, pd


@app.cell
def _(mo):
    mo.md("""
    # Exploring measurements

    Move the slider to change the number of synthetic measurements.
    The summary and table update automatically. A fixed random seed makes
    the results reproducible for each selected sample size.
    """)
    return


@app.cell
def _(mo):
    sample_size = mo.ui.slider(
        start=10, stop=200, step=10, value=50, label="Number of measurements"
    )
    sample_size
    return (sample_size,)


@app.cell
def _(np, pd, sample_size):
    measurements = np.random.default_rng(42).normal(
        loc=10.0, scale=2.0, size=sample_size.value
    )
    data = pd.DataFrame({
        "Observation": np.arange(1, len(measurements) + 1),
        "Measurement": measurements,
    })
    return data, measurements


@app.cell
def _(mean_measurement, measurements, mo):
    sample_mean = mean_measurement(measurements)
    mo.md(f"**Sample size:** {len(measurements)} — **Mean:** {sample_mean:.3f}")
    return (sample_mean,)


@app.cell
def _(data, mo):
    mo.ui.table(data)
    return


if __name__ == "__main__":
    app.run()
