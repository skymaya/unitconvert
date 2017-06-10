#!/usr/bin/python

# pylint: disable=I0011,W0108

"""Unit tests for the temperatureunits module"""

#  standard library imports
import unittest


class MassUnit(object):
    """
    Initialize a MassUnit to return the results of doconvert(), for the
    purpose of converting one mass unit to another mass unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.metric_base = 1.0  # grams in a gram
        self.imperial_base = 28.349523125  # grams in an ounce
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function)
        return function()

    def doconvert(self):
        """
        Return calculated conversion between two units

        :returns: string containing original unit and value with converted
        unit and value
        :raises ValueError: if the amount (amt) is less than 0
        """
        if self.amt < 0:
            raise ValueError('Amount must be a positive number')
        conv = (self.amt * self.getuval(self.ufrom)) / self.getuval(self.uto)
        return conv

    def unit_mg(self):
        """Return the value of one Milligram (mg)
        based on a base metric value"""
        return self.metric_base / 1000.0

    def unit_g(self):
        """Return the value of one Gram (g)
        based on a base metric value"""
        return self.metric_base

    def unit_oz(self):
        """Return the value of one Ounce (oz)
        based on a base imperial value"""
        return self.imperial_base

    def unit_lb(self):
        """Return the value of one Pound (lb)
        based on a base imperial value"""
        return self.imperial_base * 16.0

    def unit_kg(self):
        """Return the value of one Kilogram (kg)
        based on a base metric value"""
        return self.metric_base * 1000.0


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_oz2lb(self):
        """Test converting oz to lb"""
        result = round(MassUnit(16, 'oz', 'lb').doconvert(), 2)
        self.assertEqual(result, round(1.0, 2))

    def test_g2lb(self):
        """Test converting g to lb"""
        result = round(MassUnit(27, 'g', 'lb').doconvert(), 2)
        self.assertEqual(result, round(0.0595248107899, 2))

    def test_oz2mg(self):
        """Test converting oz to mg"""
        result = round(MassUnit(1, 'oz', 'mg').doconvert(), 2)
        self.assertEqual(result, round(28349.523125, 2))


class TestExceptions(unittest.TestCase):
    """Test cases to ensure providing a negative amount throws ValueError."""
    def test_oz2lb(self):
        """Test converting oz to lb"""
        result = MassUnit(-16, 'oz', 'lb')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_g2lb(self):
        """Test converting g to lb"""
        result = MassUnit(-27, 'g', 'lb')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_oz2mg(self):
        """Test converting oz to mg"""
        result = MassUnit(-1, 'oz', 'mg')
        self.assertRaises(ValueError, lambda: result.doconvert())


if __name__ == '__main__':
    unittest.main()
