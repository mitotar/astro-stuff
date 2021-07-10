import pytest
import astropy.constants as const
from src.calculations import calc_grav_acceleration, calc_escape_velocity


class TestGetGravAcceleration(object):
    def test_on_one_zero_value(self):
        """
        Test for one non-zero value.
        """

        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(0, 1)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."
        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(1, 0)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."

    def test_on_two_zero_values(self):
        """
        Test for two non-zero values.
        """

        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(0, 0)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."

    def test_on_one_negative_value(self):
        """
        Test for one negative value.
        """

        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(-1, 1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."
        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(1, -1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."

    def test_on_two_negative_values(self):
        """
        Test for two negative values.
        """

        with pytest.raises(ValueError) as e:
            calc_grav_acceleration(-1, -1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."

    def test_on_valid_values(self):
        """
        Test for proper value input.
        """

        # Earth values
        earth_theory = 9.81
        earth_calc = calc_grav_acceleration(
            5.97e24, 6.371e6)
        assert earth_calc == pytest.approx(
            earth_calc, 0.02), "Expected {0}, but got {1}.".format(earth_theory, earth_calc)
        # Jupiter values
        jupiter_theory = 23.1
        jupiter_calc = calc_grav_acceleration(1.9e27, 1.42e8 / 2)
        assert jupiter_calc == pytest.approx(
            jupiter_theory, 0.2), "Expected {0}, but got {1}.".format(jupiter_theory, jupiter_calc)
        # Sun values
        sun_theory = 274
        sun_calc = calc_grav_acceleration(1.99e30, 6.957e8)
        assert sun_calc == pytest.approx(
            sun_theory, 0.2), "Expected {0}, but got {1}.".format(sun_theory, sun_calc)

    def test_on_valid_values_earth_units(self):
        # Earth values
        earth_theory = 9.81
        earth_calc = calc_grav_acceleration(
            1, 1, earth_units=True)
        assert earth_calc == pytest.approx(
            earth_calc, 0.02), "Expected {0}, but got {1}.".format(earth_theory, earth_calc)
        # Jupiter values
        jupiter_theory = 23.1
        jupiter_calc = calc_grav_acceleration(
            const.M_jup.value / const.M_earth.value, const.R_jup.value / const.R_earth.value, earth_units=True)
        assert jupiter_calc == pytest.approx(
            jupiter_theory, 0.2), "Expected {0}, but got {1}.".format(jupiter_theory, jupiter_calc)
        # Sun values
        sun_theory = 274
        sun_calc = calc_grav_acceleration(
            const.M_sun.value / const.M_earth.value, const.R_sun.value / const.R_earth.value, earth_units=True)
        assert sun_calc == pytest.approx(
            sun_theory, 0.2), "Expected {0}, but got {1}.".format(sun_theory, sun_calc)


class TestCalcEscapeVelocity(object):
    def test_on_one_zero_value(self):
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(0, 1)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(1, 0)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."

    def test_on_two_zero_values(self):
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(0, 0)
        assert e.match(
            "Mass and radius values must be non-zero."), "Expected ValueError."

    def test_on_one_negative_value(self):
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(-1, 1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(1, -1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."

    def test_on_two_negative_values(self):
        with pytest.raises(ValueError) as e:
            calc_escape_velocity(-1, -1)
        assert e.match(
            "Mass and radius values must be positive."), "Expected ValueError."

    def test_on_valid_values(self):
        # Earth values
        earth_theory = 11.2e3
        earth_calc = calc_escape_velocity(5.97e24, 6.371e6)
        assert earth_calc == pytest.approx(
            earth_theory, 0.2), "Expected {0}, but got {1}.".format(earth_theory, earth_calc)
        # Jupiter values
        jupiter_theory = 59.5e3
        jupiter_calc = calc_escape_velocity(1.9e27, 1.42e8 / 2)
        assert jupiter_calc == pytest.approx(
            jupiter_theory, 0.2), "Expected {0}, but got {1}.".format(jupiter_theory, jupiter_calc)
        # Sun values
        sun_theory = 615e3
        sun_calc = calc_escape_velocity(1.99e30, 6.957e8)
        assert sun_calc == pytest.approx(
            sun_theory, 2), "Expected {0}, but got {1}.".format(sun_theory, sun_calc)

    def test_on_valid_values_earth_units(self):
        # Earth values
        earth_theory = 11.2e3
        earth_calc = calc_escape_velocity(1, 1, earth_units=True)
        assert earth_calc == pytest.approx(
            earth_theory, 0.2), "Expected {0}, but got {1}.".format(earth_theory, earth_calc)
        # Jupiter values
        jupiter_theory = 59.5e3
        jupiter_calc = calc_escape_velocity(
            const.M_jup.value / const.M_earth.value, const.R_jup.value / const.R_earth.value, earth_units=True)
        assert jupiter_calc == pytest.approx(
            jupiter_theory, 0.2), "Expected {0}, but got {1}.".format(jupiter_theory, jupiter_calc)
        # Sun values
        sun_theory = 615e3
        sun_calc = calc_escape_velocity(
            const.M_sun.value / const.M_earth.value, const.R_sun.value / const.R_earth.value, earth_units=True)
        assert sun_calc == pytest.approx(
            sun_theory, 2), "Expected {0}, but got {1}.".format(sun_theory, sun_calc)
