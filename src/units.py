import regex as re


def au_to_ly(au):
    if au < 0:
        raise ValueError("AU value must be non-negative.")

    return au / 63241


def au_to_pc(au):
    if au < 0:
        raise ValueError("AU value must be non-negative.")

    return au * 4.84814e-6


def ly_to_au(ly):
    if ly < 0:
        raise ValueError("Light-year value must be non-negative.")

    return ly * 63241


def ly_to_pc(ly):
    if ly < 0:
        raise ValueError("Light-year value must be non-negative.")

    return ly / 3.26


def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature must be non-negative.")
    return kelvin - 273.15


def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError(
            "Temperature must be greater than absolute zero (-273.15 K).")
    return celsius + 273.15
