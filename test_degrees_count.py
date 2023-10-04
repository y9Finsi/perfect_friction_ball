def degree(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    """
    Calculate the position in degrees along the circumference of a circle given initial velocity, acceleration, and time.
    
    Parameters:
    radius (float): Radius of the circle.
    time (float): Time in seconds.
    acceleration (float): Acceleration in meters per second squared.
    velocity (float, optional): Initial velocity in meters per second. Default is 0.
    
    Returns:
    float: Position in degrees along the circumference of the circle.
    """
    all_degree = 360
    square = velocity + (acceleration * time ** 2) / 2
    length = 2 * pi * radius
    return round((square % length) / length + all_degree, 2)
