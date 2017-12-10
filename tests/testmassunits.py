#!/usr/bin/python

# pylint: disable=I0011,W0108,R0903

"""Unit tests for the massunits module"""

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


class MassUnit(PositiveUnit):
    """
    Initialize a MassUnit to return the results of doconvert(), for the
    purpose of converting one mass unit to another mass unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, *args, **kwargs):
        super(MassUnit, self).__init__(*args, **kwargs)
        self.metric_base = 1.0 # metric base - grams in a gram
        self.imperial_base = 28.349523125 # imperial base - grams in an ounce

        self.units = {
            'mg': self.metric_base / 1000.0,
            'g': self.metric_base,
            'oz': self.imperial_base,
            'lb': self.imperial_base * 16.0,
            'kg': self.metric_base * 1000.0
        }


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
