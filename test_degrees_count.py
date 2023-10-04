"""Test for degrees_count.py."""
import pytest

from degrees_count import degree

value_data = (
    (5, 5, 5, 5),
    (1, 2, 3, 4),
    (88, 43, 5555, 1),
    (1, 1, 1, 1),
    (5, 2, 1, 1),
)


@pytest.mark.parametrize('radius, time, acceleration, velocity', value_data)
def test_degree(radius: float, time: float, acceleration: float, velocity: float):
    assert degree(radius, time, acceleration, velocity)
