import pytest
from project.main import mean_measurement


def test_mean_measurement():
    assert mean_measurement([2, 4, 6]) == pytest.approx(4)


@pytest.mark.parametrize("values", [[], [float("nan")], [float("inf")], [[1, 2]]])
def test_invalid_measurements(values):
    with pytest.raises(ValueError):
        mean_measurement(values)
