import astropy.constants as const
import math


def stefan_boltzmann(area, temp):
    """
    Calculate the luminosity (W) of a spherical blackbody with the given surface area (m^2) and temperature (K) using the Stefan_boltzmann law.
    """
    if temp == 0:
        raise ValueError("Temperature must be greater than 0.")
    if area < 0 or temp < 0:
        raise ValueError("Area and temperature values must be non-negative.")
    return const.sigma_sb.value * area * temp ** 4


def brightness(lum, dist):
    """
    Calculate the brightness of an object with the given luminosity (W) at the given distance away (m).
    """

    if lum <= 0 or dist <= 0:
        raise ValueError(
            "Luminosity and distance values must be greater than 0.")
    return lum / (4 * math.pi * dist ** 2)


def get_peak_wavelength(temp):
    """
    Give approximate peak wavelength (m) of a blackbody object with the given temperature (K).
    """

    if temp <= 0:
        raise ValueError("Temperature must be non-negative.")
    return 2.9e-3 / temp


def wavelength_to_color(l):
    """
    Outputs the part of the EM spectrum of the input wavelength. Assumed input value is in meters.
    """

    if l <= 0:
        raise ValueError("Wavelength must be non-negative.")
    if l < 1e-12:
        print("gamma rays")
    elif l < 1e-8:
        print("X-rays")
    elif l < 1e-7:
        print("ultraviolet")
    elif l < 7.5e-7:
        print("visible ", end="", flush=True)
        if l < 4.5e-7:
            print("(violet)")
        elif l < 4.95e-7:
            print("(blue)")
        elif l < 5.7e-7:
            print("(green)")
        elif l < 5.9e-7:
            print("(yellow)")
        elif l < 6.2e-7:
            print("(orange)")
        else:
            print("(red)")
    elif l < 1e-3:
        print("infrared")
    elif l < 1e-1:
        print("microwave")
    else:
        print("radio")
