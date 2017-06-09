#!/usr/bin/python

# pylint: skip-file

import unittest


class TemperatureUnit(object):
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def getuval(self, argument):
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function)
        return function()

    def doconvert(self):
        conv = self.getuval(self.ufrom)[self.uto]
        return str(conv)

    def unit_F(self):
        calc = {
            'C': (self.amt - 32.0) * 5 / 9,
            'K': (self.amt + 459.67) * 5 / 9,
            'F': self.amt
        }
        return calc

    def unit_C(self):
        calc = {
            'F': (self.amt * 9) / 5 + 32.0,
            'K': self.amt + 273.15,
            'C': self.amt
        }
        return calc

    def unit_K(self):
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
        result = TemperatureUnit(32, 'F', 'C').doconvert()
        self.assertEqual(result, '0.0')

    def test_f2k(self):
        result = TemperatureUnit(5, 'F', 'K').doconvert()
        self.assertEqual(result, '258.15')

    def test_k2c(self):
        result = TemperatureUnit(34, 'K', 'C').doconvert()
        self.assertEqual(result, '-239.15')


class TestOutput(unittest.TestCase):
    """Test cases to check unit function output; must be a dictionary with a
    length of 3. Passing ufrom and uto aren't necessary so those are replaced
    with None."""
    def test_unit_F(self):
        result = TemperatureUnit(34, None, None).unit_F()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)

    def test_unit_C(self):
        result = TemperatureUnit(34, None, None).unit_C()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)

    def test_unit_K(self):
        result = TemperatureUnit(34, None, None).unit_K()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
