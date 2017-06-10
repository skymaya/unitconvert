#!/usr/bin/python

# pylint: disable=I0011,W0108

"""Unit tests for the volumeunits module"""

#  standard library imports
import unittest


class VolumeUnit(object):
    """
    Initialize a VolumeUnit to return the results of doconvert(), for the
    purpose of converting one volume unit to another volume unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.metric_base = 1.0  # milliliters in a milliliter
        self.us_base = 4.92892159  # milliliters in a teaspoon
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

    def unit_ml(self):
        """Return the value of one Milliliter (ml)
        based on a base metric value"""
        return self.metric_base

    def unit_tsp(self):
        """Return the value of one Teaspoon (tsp)
        based on a base us value"""
        return self.us_base

    def unit_tbsp(self):
        """Return the value of one Tablespoon (tbsp)
        based on a base us value"""
        return self.us_base * 3.0

    def unit_cup(self):
        """Return the value of one Cup (cup)
        based on a base us value"""
        return self.us_base * 48.0

    def unit_pt(self):
        """Return the value of one Pint (pt)
        based on a base us value"""
        return self.us_base * 96.0

    def unit_qt(self):
        """Return the value of one Quart (qt)
        based on a base us value"""
        return self.us_base * 192.0

    def unit_gal(self):
        """Return the value of one Gallon (gal)
        based on a base us value"""
        return self.us_base * 768.0

    def unit_l(self):
        """Return the value of one Liter (l)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def unit_in3(self):
        """Return the value of one Cubic Inch (in3)
        based on a base us value"""
        return (self.us_base * 768.0) / 231

    def unit_ft3(self):
        """Return the value of one Cubic Foot (ft3)
        based on a base us value"""
        return ((self.us_base * 768.0) / 231) * 1728


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_gal2in3(self):
        """Test converting gal to in3"""
        result = round(VolumeUnit(5.6, 'gal', 'in3').doconvert(), 2)
        self.assertEqual(result, round(1293.6, 2))

    def test_ml2cup(self):
        """Test converting ml to cup"""
        result = round(VolumeUnit(56, 'ml', 'cup').doconvert(), 2)
        self.assertEqual(result, round(0.236698, 2))

    def test_tbsp2l(self):
        """Test converting tbsp to l"""
        result = round(VolumeUnit(4.7, 'tbsp', 'l').doconvert(), 4)
        self.assertEqual(result, round(0.0694978, 4))


class TestExceptions(unittest.TestCase):
    """Test cases to ensure providing a negative amount throws ValueError."""
    def test_gal2in3(self):
        """Test converting gal to in3"""
        result = VolumeUnit(-4, 'gal', 'in3')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_ml2cup(self):
        """Test converting ml to cup"""
        result = VolumeUnit(-5, 'ml', 'cup')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_tbsp2l(self):
        """Test converting tbsp to l"""
        result = VolumeUnit(-8, 'tbsp', 'l')
        self.assertRaises(ValueError, lambda: result.doconvert())


if __name__ == '__main__':
    unittest.main()
