import unittest

from math import pi
from circle_area import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2), pi * (2**2))

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raise when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")