#!/usr/bin/python

# pylint: disable=I0011,W0108,R0903

"""Unit tests for the lengthunits module"""

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


class LengthUnit(PositiveUnit):
    """
    Initialize a LengthUnit to return the results of doconvert(), for the
    purpose of converting one length unit to another length unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, *args, **kwargs):
        super(LengthUnit, self).__init__(*args, **kwargs)
        self.metric_base = 1.0 # millimeters in a millimeter
        self.imperial_base = 25.4000508001 # millimeters in an inch

        self.units = {
            'mm': self.metric_base,
            'cm': self.metric_base * 10.0,
            'in': self.imperial_base,
            'ft': self.imperial_base * 12.0,
            'yd': self.imperial_base * 36.0,
            'm': self.metric_base * 1000.0,
            'km': self.metric_base * 1000000.0,
            'mi': self.imperial_base * 63360.0
        }


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_in2mm(self):
        """Test converting in to mm"""
        result = round(LengthUnit(5.0, 'in', 'mm').doconvert(), 2)
        self.assertEqual(result, round(127.0, 2))

    def test_mi2km(self):
        """Test converting mi to km"""
        result = round(LengthUnit(3.4, 'mi', 'km').doconvert(), 2)
        self.assertEqual(result, round(5.47177, 2))

    def test_ft2in(self):
        """Test converting ft to in"""
        result = round(LengthUnit(2.5, 'ft', 'in').doconvert(), 2)
        self.assertEqual(result, round(30.0, 2))


class TestExceptions(unittest.TestCase):
    """Test cases to ensure providing a negative amount throws ValueError."""
    def test_in2mm(self):
        """Test converting in to mm"""
        result = LengthUnit(-5.0, 'in', 'mm')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_mi2km(self):
        """Test converting mi to km"""
        result = LengthUnit(-3.4, 'mi', 'km')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_ft2in(self):
        """Test converting ft to in"""
        result = LengthUnit(-2.5, 'ft', 'in')
        self.assertRaises(ValueError, lambda: result.doconvert())


if __name__ == '__main__':
    unittest.main()
