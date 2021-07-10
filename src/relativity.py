import astropy.constants as const
import math


def lorentz_factor(v, c_units=True):
    """
    Calculates the Lorentz factor for the given velocity.
    Note: If c_units=False, then 299792458 is used as the speed of light, c, NOT, 3e8.
    """

    v = abs(v)  # account for negative input
    if (c_units and v > 1) or (not c_units and v > const.c.value):
        raise ValueError(
            "Speed must be less than the speed of light in a vacuum.")
    if c_units:
        frac = v
    else:
        frac = v / const.c.value

    return math.sqrt(1 - frac ** 2)
