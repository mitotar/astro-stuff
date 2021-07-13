import pytest
import astropy.constants as const
import src.luminosity_brightness as lb


class TestStefanBoltzmann(object):
    def test_negative_area_negative_temp(self):
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(-10, -2000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(-1e30, -5000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_negative_area_positive_temp(self):
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(-10, 2000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(-1e30, 5000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_positive_area_negative_temp(self):
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(10, -2000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = lb.stefan_boltzmann(1e30, -5000)
        assert e.match(
            "Area and temperature values must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_positive_area_positive_temp(self):
        theory = 0.00567
        calc = lb.stefan_boltzmann(10, 10)
        assert calc == pytest.approx(
            theory, 1e-4), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 5.67e20
        calc = lb.stefan_boltzmann(1e20, 1000)
        assert calc == pytest.approx(
            theory, 1e18), "Expected {0}, but got {1}.".format(theory, calc)
