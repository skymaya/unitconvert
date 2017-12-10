#!/usr/bin/python

# pylint: disable=I0011,W0108,R0903

"""Unit tests for the volumeunits module"""

#  standard library imports
import unittest


class PositiveUnit(object):
    """docstring"""
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

        self.units = {}

    def doconvert(self):
        """
        Return calculated conversion between two units

        :returns: string containing original unit and value with converted
        unit and value
        :raises ValueError: if the amount (amt) is less than 0
        """
        if self.amt < 0:
            raise ValueError('Amount must be a positive number')
        conv = (self.amt * self.units[self.ufrom]) / self.units[self.uto]
        return conv


class VolumeUnit(PositiveUnit):
    """
    Initialize a VolumeUnit to return the results of doconvert(), for the
    purpose of converting one volume unit to another volume unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, *args, **kwargs):
        super(VolumeUnit, self).__init__(*args, **kwargs)
        self.metric_base = 1.0  # milliliters in a milliliter
        self.us_customary_base = 4.92892159375  # milliliters in a teaspoon
        self.us_legal_base = 5.0  # milliliters in a teaspoon
        self.imperial_base = 5.916666666666667  # milliliters in a teaspoon

        self.units = {
            'ml': self.metric_base,
            'tsp': self.us_customary_base,
            'tbsp': self.us_customary_base * 3.0,
            'floz': self.us_customary_base * 6.0,
            'cup': self.us_customary_base * 48.0,
            'lcup': self.us_legal_base * 48.0,
            'pt': self.us_customary_base * 96.0,
            'qt': self.us_customary_base * 192.0,
            'gal': self.us_customary_base * 768.0,
            'l': self.metric_base * 1000.0,
            'in3': (self.us_customary_base * 768.0) / 231,
            'ft3': ((self.us_customary_base * 768.0) / 231) * 1728
        }


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

    def test_lcup2l(self):
        """Test converting tbsp to l"""
        result = round(VolumeUnit(1, 'lcup', 'l').doconvert(), 4)
        self.assertEqual(result, round(0.24, 4))

    def test_cup2floz(self):
        """Test converting cup to floz"""
        result = round(VolumeUnit(1, 'cup', 'floz').doconvert(), 4)
        self.assertEqual(result, round(8.0, 4))


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
