#!/usr/bin/python

"""Unit tests for the temperatureunits module"""

# pylint: disable=I0011,C0103,R0903

import unittest


class TemperatureUnit(object):
    """
    Initialize a TemperatureUnit to return the results of doconvert(), for the
    purpose of converting one temperature unit to another temperature unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function)
        return function()

    def doconvert(self):
        """Return string containing converted value"""
        conv = self.getuval(self.ufrom)[self.uto]
        return "{0}".format(conv)

    def unit_F(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from F to F, C, and K"""
        calc = {
            'C': (self.amt - 32.0) * 5 / 9,
            'K': (self.amt + 459.67) * 5 / 9,
            'F': self.amt
        }
        return calc

    def unit_C(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from C to F, C, and K"""
        calc = {
            'F': (self.amt * 9) / 5 + 32.0,
            'K': self.amt + 273.15,
            'C': self.amt
        }
        return calc

    def unit_K(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from K to F, C, and K"""
        if self.amt < 0:
            raise ValueError('Amount must be a positive number')
        calc = {
            'F': (self.amt * 9) / 5 - 459.67,
            'C': self.amt - 273.15,
            'K': self.amt
        }
        return calc


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_f2c(self):
        """Test converting F to C"""
        result = TemperatureUnit(32, 'F', 'C').doconvert()
        self.assertEqual(result, '0.0')

    def test_f2k(self):
        """Test converting F to K"""
        result = TemperatureUnit(5, 'F', 'K').doconvert()
        self.assertEqual(result, '258.15')

    def test_k2c(self):
        """Test converting K to C"""
        result = TemperatureUnit(34, 'K', 'C').doconvert()
        self.assertEqual(result, '-239.15')


class TestOutput(unittest.TestCase):
    """Test cases to check unit function output; must be a dictionary with a
    length of 3. Passing ufrom and uto aren't necessary so those are replaced
    with None."""
    def test_unit_F(self):
        """Test output of unit_F"""
        result = TemperatureUnit(34, None, None).unit_F()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)

    def test_unit_C(self):
        """Test output of unit_C"""
        result = TemperatureUnit(34, None, None).unit_C()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)

    def test_unit_K(self):
        """Test output of unit_K"""
        result = TemperatureUnit(34, None, None).unit_K()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
