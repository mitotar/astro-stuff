import astropy.constants as const
import math


def calc_grav_acceleration(mass, radius, earth_units=False):
    """
    Calculates the magnitude of the acceleration (m /s^2) due to gravity of a spherical body with the given mass and radius.
    Assumes mass and radius are in meters and kilograms, respectively, unless earth_units=True, in which case they are treated as Earth masses and Earth radii, respectively.
    """

    if mass == 0 or radius == 0:
        raise ValueError("Mass and radius values must be non-zero.")
    if mass < 0 or radius < 0:
        raise ValueError("Mass and radius values must be positive.")

    if earth_units:
        mass = mass * const.M_earth.value
        radius = radius * const.R_earth.value

    return const.G.value * mass / radius ** 2


def calc_escape_velocity(mass, radius, earth_units=False):
    """
    Calculates the magnitude of the escape velocity (m/s) of a circular body with the given mass and radius.
    Assumes mass and radius are in meters and kilograms, respectively, unless earth_units=True, in which case they are treated as Earth masses and Earth radii, respectively.
    """

    if mass == 0 or radius == 0:
        raise ValueError("Mass and radius values must be non-zero.")
    if mass < 0 or radius < 1:
        raise ValueError("Mass and radius values must be positive.")

    if earth_units:
        mass = mass * const.M_earth.value
        radius = radius * const.R_earth.value

    return math.sqrt(2 * const.G.value * mass / radius)
