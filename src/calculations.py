import astropy.constants as const
import math


def calc_grav_acceleration(mass, radius):
    """
    Calculates the magnitude of the acceleration (m /s^2) due to gravity of a spherical body with the given mass (kg) and radius (m).
    """

    if mass == 0 or radius == 0:
        raise ValueError("Mass and radius values must be non-zero.")
    if mass < 0 or radius < 0:
        raise ValueError("Mass and radius values must be positive.")
    return const.G.value * mass / radius ** 2


def calc_escape_velocity(mass, radius):
    """
    Calculates the escape velocity (m/s) of a circular body with the given mass (kg) and radius (m).
    """

    if mass == 0 or radius == 0:
        raise ValueError("Mass and radius values must be non-zero.")
    if mass < 0 or radius < 1:
        raise ValueError("Mass and radius values must be positive.")
    return math.sqrt(2 * const.G.value * mass / radius)
