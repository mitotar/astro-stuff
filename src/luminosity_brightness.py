import astropy.constants as const


def stefan_boltzmann(area, temp):
    """
    Calculate the luminosity (W) of a spherical blackbody with the given surface area (m^2) and temperature (K) using the Stefan_boltzmann law.
    """
    if area < 0 or temp < 0:
        raise ValueError("Area and temperature values must be non-negative.")
    return const.sigma_sb.value * area * temp ** 4


def get_peak_wavelength(temp):
    """
    Give approximate peak wavelength (mm) of a blackbody object with the given temperature (K).
    """

    if temp <= 0:
        raise ValueError("Temperature must be non-negative.")
    return 2.9 / temp
