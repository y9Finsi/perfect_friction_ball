"""A module for testing the `degree` function in the `degrees_count` module."""
import pytest

from degrees_count import degree

value_data = (
    ((10.01, 6.9, 2.4, 6.3), 215.83),
    ((6.1, 47.92, 9.89, 20.02), 108.84),
    ((9.11, 9.99, 7.77, 8.88), 116.45),
    ((7.16, 42.74, 9.29, 7.22), 168.5),
)


@pytest.mark.parametrize('radius, time, acceleration, velocity', value_data)
def test_degree(radius: float, time: float, acceleration: float, velocity: float, expected: float):
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
    assert degree(radius, time, acceleration, velocity) == expected
