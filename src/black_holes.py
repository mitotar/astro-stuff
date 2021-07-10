import astropy.constants as const


def schwarzschild_radius(mass, solar_units=False):
    """
    Calculate the Schwarzschild radius of a singularity with the given mass.
    Assumes the mass is in kilograms, unless solar_units=True, in which case it is treated as solar masses.
    """

    if mass < 0:
        raise ValueError("Mass value must be non-negative.")

    if solar_units:
        mass = mass * const.M_sun.value

    return 2 * const.G.value * mass / (const.c.value ** 2)
