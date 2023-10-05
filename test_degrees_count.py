"""A module for testing the `degree` function in the `degrees_count` module."""
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
    """
    Test the 'degree' function with various input parameters.

    Args:
        radius: Radius of the circle.
        time: Time in seconds.
        acceleration: Acceleration in meters per second squared.
        velocity: Initial velocity in meters per second.

    Asserts:
        True if the `degree` function returns expected results for the given input parameters.
    """
    assert degree(radius, time, acceleration, velocity)
