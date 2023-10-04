""""""
from math import pi


def degree(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    all_degree = 360
    square = velocity + (acceleration * time ** 2) / 2
    length = 2 * pi * radius
    return round((square % length) / length + all_degree, 2)
