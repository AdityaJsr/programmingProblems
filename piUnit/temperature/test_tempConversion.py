"""
title - This is the test case for the tempConversion program.
author name - Aditya Kumar
creation time - 23 ‎February ‎2021, 22:23:24
modified time - ‎24 ‎February ‎2021, ‏‎11:23:24

"""

import unittest
from main.tempConversion import *

class TestTemp(unittest.TestCase):

    def test_celsiusToFahrenheit(self):
        result = celsiusToFahrenheit(50)
        self.assertEqual(result, 122)
        result = celsiusToFahrenheit(-5)
        self.assertEqual(result, 23)
        result = celsiusToFahrenheit(999)
        self.assertEqual(result, 1830)
        result = celsiusToFahrenheit(0)
        self.assertEqual(result, 32)

    def test_fahrenhietToCelsius(self):
        result = fahrenhietToCelsius(122)
        self.assertEqual(result, 50)
        result = fahrenhietToCelsius(23)
        self.assertEqual(result, -5)
        result = fahrenhietToCelsius(1830)
        self.assertEqual(result, 999)
        result = fahrenhietToCelsius(32)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()