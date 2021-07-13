import pytest
import astropy.constants as const
import src.units as units


class TestAUToLY(object):

    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.au_to_ly(-2.3e10)
        assert e.match(
            "AU value must be non-negative."), "Expected ValueError, but got {0}".format(calc)
        with pytest.raises(ValueError) as e:
            calc = units.au_to_ly(-1)
        assert e.match(
            "AU value must be non-negative."), "Expected ValueError, but got {0}".format(calc)

    def test_on_zero_value(self):
        calc = units.au_to_ly(0)
        assert calc == 0, "Expected {0}, but got {1}".format(
            0, calc)

    def test_on_valid_value(self):
        # Value of 1 light-year
        theory = 1
        calc = units.au_to_ly(63241)
        assert calc == pytest.approx(
            theory, 0.2), "Expected {0}, but got {1}".format(theory, calc)
        # Value of 1 parsec
        theory = 3.26
        calc = units.au_to_ly(206165.9)
        assert calc == pytest.approx(
            theory, 2), "Expected {0}, but got {1}".format(theory, calc)


class TestLYToAU(object):

    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.ly_to_au(-2.3e10)
        assert e.match(
            "Light-year value must be non-negative."), "Expected ValueError, but got {0}".format(calc)
        with pytest.raises(ValueError) as e:
            calc = units.ly_to_au(-1)
        assert e.match(
            "Light-year value must be non-negative."), "Expected ValueError, but got {0}".format(calc)

    def test_on_zero_value(self):
        calc = units.ly_to_au(0)
        assert calc == 0, "Expected {0}, but got {1}".format(
            0, calc)

    def test_on_valid_value(self):
        # Value of 1 light-year
        theory = 63241
        calc = units.ly_to_au(1)
        assert calc == pytest.approx(
            theory, 2), "Expected {0}, but got {1}".format(theory, calc)
        # Value of 1 parsec
        theory = 206165.9
        calc = units.ly_to_au(3.26)
        assert calc == pytest.approx(
            theory, 2), "Expected {0}, but got {1}".format(theory, calc)


class TestAUToPC(object):
    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.au_to_pc(-2.3e10)
        assert e.match(
            "AU value must be non-negative."), "Expected ValueError, but got {0}".format(calc)
        with pytest.raises(ValueError) as e:
            calc = units.au_to_pc(-1)
        assert e.match(
            "AU value must be non-negative."), "Expected ValueError, but got {0}".format(calc)

    def test_on_zero_value(self):
        calc = units.au_to_pc(0)
        assert calc == 0, "Expected {0}, but got {1}".format(
            0, calc)

    def test_on_valid_value(self):
        # Value of 1 AU
        theory = 4.84814e-6
        calc = units.au_to_pc(1)
        assert calc == pytest.approx(theory, 0.02), "Expected {0}, but got {1}".format(
            theory, calc)
        # Value of 1 pc
        theory = 1
        calc = units.au_to_pc(206265)
        assert calc == pytest.approx(theory, 0.02), "Expected {0}, but got {1}".format(
            theory, calc)


class TestLYToPC(object):
    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.ly_to_pc(-2.3e10)
        assert e.match(
            "Light-year value must be non-negative."), "Expected ValueError, but got {0}".format(calc)
        with pytest.raises(ValueError) as e:
            calc = units.ly_to_pc(-1)
        assert e.match(
            "Light-year value must be non-negative."), "Expected ValueError, but got {0}".format(calc)

    def test_on_zero_value(self):
        calc = units.ly_to_pc(0)
        assert calc == 0, "Expected {0}, but got {1}".format(
            0, calc)

    def test_on_valid_value(self):
        # Value of 1 ly
        theory = 1 / 3.26
        calc = units.ly_to_pc(1)
        assert calc == pytest.approx(theory, 0.02), "Expected {0}, but got {1}".format(
            theory, calc)
        # Value of 1 pc
        theory = 1
        calc = units.ly_to_pc(3.26)
        assert calc == pytest.approx(theory, 0.02), "Expected {0}, but got {1}".format(
            theory, calc)


class TestKelvinToCelsius(object):
    def test_on_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.kelvin_to_celsius(-1)
        assert e.match(
            "Temperature must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_valid_value(self):
        theory = -273.15
        calc = units.kelvin_to_celsius(0)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0
        calc = units.kelvin_to_celsius(273.15)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 6000
        calc = units.kelvin_to_celsius(6273.15)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)


class TestCelsiusToKelvin(object):
    def test_on_invalid_value(self):
        with pytest.raises(ValueError) as e:
            calc = units.celsius_to_kelvin(-273.2)
        assert e.match(
            # including () in the match string caused issues so I just check for the beginning of the string
            "Temperature must be greater than absolute zero"), "Expected ValueError, but got {0}.".format(calc)

    def test_on_valid_value(self):
        theory = 0
        calc = units.celsius_to_kelvin(-273.15)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 273.15
        calc = units.celsius_to_kelvin(0)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 6273.15
        calc = units.celsius_to_kelvin(6000)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
