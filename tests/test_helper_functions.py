import pytest
import math
import src.helper_functions as hf


class TestGetSurfaceArea(object):
    def test_on_negative_radius(self):
        with pytest.raises(ValueError) as e:
            calc = hf.get_surface_area(-20)
        assert e.match(
            "Radius value must be non-negative."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = hf.get_surface_area(-1e20)
        assert e.match(
            "Radius value must be non-negative."), "Expected ValueError, but got {0}.".format(calc)
        with pytest.raises(ValueError) as e:
            calc = hf.get_surface_area(-1e-9)
        assert e.match(
            "Radius value must be non-negative."), "Expected ValueError, but got {0}.".format(calc)

    def test_on_positive_radius(self):
        theory = 0
        calc = hf.get_surface_area(0)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 5026.55
        calc = hf.get_surface_area(20)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 1.26e41
        calc = hf.get_surface_area(1e20)
        assert calc == pytest.approx(
            theory, 1e39), "Expected {0}, but got {1}.".format(theory, calc)
        theory = 1.25664e-17
        calc = hf.get_surface_area(1e-9)
        assert calc == pytest.approx(
            theory), "Expected {0}, but got {1}.".format(theory, calc)
