
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
