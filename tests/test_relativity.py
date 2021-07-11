import pytest
import astropy.constants as const
import src.relativity as rel


class TestLorentzFactor(object):
    def test_on_postive_valid_value_c_units(self):
        theory = 0.999999995
        calc = rel.lorentz_factor(0.0001, c_units=True)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0.866
        calc = rel.lorentz_factor(0.5, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 4.472e-3
        calc = rel.lorentz_factor(0.99999, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0
        calc = rel.lorentz_factor(1, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)

    def test_on_negative_valid_value_c_units(self):
        theory = 0.999999995
        calc = rel.lorentz_factor(-0.0001, c_units=True)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0.866
        calc = rel.lorentz_factor(-0.5, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 4.472e-3
        calc = rel.lorentz_factor(-0.99999, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0
        calc = rel.lorentz_factor(-1, c_units=True)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)

    def test_on_positive_valid_value(self):
        theory = 0.999999995
        calc = rel.lorentz_factor(0.0001 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0.866
        calc = rel.lorentz_factor(0.5 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 4.472e-3
        calc = rel.lorentz_factor(0.99999 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0
        calc = rel.lorentz_factor(const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)

    def test_on_negative_valid_value(self):
        theory = 0.999999995
        calc = rel.lorentz_factor(-0.0001 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0.866
        calc = rel.lorentz_factor(-0.5 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 4.472e-3
        calc = rel.lorentz_factor(-0.99999 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 0
        calc = rel.lorentz_factor(-1 * const.c.value, c_units=False)
        assert calc == pytest.approx(
            theory, 0.02), "Expected {0}, but got {1}.".format(theory, calc)

    def test_on_positive_invalid_value_c_units(self):
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(1.1, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(1.5, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(2, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_negative_invalid_value_c_units(self):
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-1.1, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-1.5, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-2, c_units=True)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_positive_invalid_value(self):
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(1.1 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(1.5 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(2 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_negative_invalid_value(self):
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-1.1 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-1.5 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = rel.lorentz_factor(-2 * const.c.value, c_units=False)
        assert e.match(
            "Speed must be less than the speed of light in a vacuum."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_zero_value(self):
        theory = 1
        calc = rel.lorentz_factor(0, c_units=True)
        assert calc == theory, "Expected {0}, but got {1}.".format(
            theory, calc)
        calc = rel.lorentz_factor(0, c_units=False)
        assert calc == theory, "Expected {0}, but got {1}.".format(
            theory, calc)


class TestLorentzContraction(self):
    def test_on_negative_x_value(self):
        pass
