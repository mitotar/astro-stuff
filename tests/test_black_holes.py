import pytest
import astropy.constants as const
import src.black_holes as bh


class TestSchwarzschildRadius(object):
    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = bh.schwarzschild_radius(-1)
            calc = bh.schwarzschild_radius(-10e30)
        assert e.match(
            "Mass value must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_zero_value(self):
        calc = bh.schwarzschild_radius(0)
        assert calc == 0, "Expected {0}, but got {1}.".format(0, calc)

    def test_on_valid_value(self):
        # Value of Sun
        theory = 2949
        calc = bh.schwarzschild_radius(const.M_sun.value)
        assert calc == pytest.approx(
            theory, 5), "Expected {0}, but got {1}.".format(theory, calc)
        # Value of Sgr A*
        theory = 1.18e10
        calc = bh.schwarzschild_radius(const.M_sun.value * 4e6)
        assert calc == pytest.approx(
            theory, 1e2), "Expected {0}, but got {1}.".format(theory, calc)
        # Value of TON 618
        theory = 1.9e14
        calc = bh.schwarzschild_radius(66e9 * const.M_sun.value)
        assert calc == pytest.approx(
            theory, 1e10), "Expected {0}, but got {1}.".format(theory, calc)

    def test_on_valid_value_solar_units(self):
        # Value of Sun
        theory = 2949
        calc = bh.schwarzschild_radius(1, solar_units=True)
        assert calc == pytest.approx(
            theory, 5), "Expected {0}, but got {1}.".format(theory, calc)
        # Value of Sgr A*
        theory = 1.18e10
        calc = bh.schwarzschild_radius(4e6, solar_units=True)
        assert calc == pytest.approx(
            theory, 1e2), "Expected {0}, but got {1}.".format(theory, calc)
        # Value of TON 618
        theory = 1.9e14
        calc = bh.schwarzschild_radius(66e9, solar_units=True)
        assert calc == pytest.approx(
            theory, 1e10), "Expected {0}, but got {1}.".format(theory, calc)
