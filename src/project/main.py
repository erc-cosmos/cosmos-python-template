"""A small example: run with python -m project.main."""
import numpy as np


def mean_measurement(values):
    """Return the mean of a non-empty sequence of finite measurements."""
    measurements = np.asarray(values, dtype=float)
    if measurements.ndim != 1 or measurements.size == 0:
        raise ValueError("Provide a non-empty sequence of measurements")
    if not np.isfinite(measurements).all():
        raise ValueError("Measurements must be finite")
    return float(np.mean(measurements))


def main():
    print(f"Mean measurement: {mean_measurement([2, 4, 6]):.2f}")


if __name__ == "__main__":
    main()
