import math


def get_surface_area(radius):
    """
    Calculate the surface area of a sphere with the given radius (m).
    """

    if radius < 0:
        raise ValueError("Radius value must be non-negative.")
    return 4 * math.pi * radius ** 2
