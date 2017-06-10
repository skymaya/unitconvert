#!/usr/bin/python

# pylint: disable=I0011,W0108

"""Unit tests for the lengthunits module"""

#  standard library imports
import unittest


class LengthUnit(object):
    """
    Initialize a LengthUnit to return the results of doconvert(), for the
    purpose of converting one length unit to another length unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.imperial_base = 25.4000508001  # millimeters in an inch
        self.metric_base = 1.0  # millimeters in a millimeter
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

    def unit_mm(self):
        """Return the value of one Millimeter (mm)
        based on a base metric value"""
        return self.metric_base

    def unit_cm(self):
        """Return the value of one Centimeter (cm)
        based on a base metric value"""
        return self.metric_base * 10.0

    def unit_in(self):
        """Return the value of one Inch (in)
        based on a base imperial value"""
        return self.imperial_base

    def unit_ft(self):
        """Return the value of one Foot (ft)
        based on a base imperial value"""
        return self.imperial_base * 12.0

    def unit_yd(self):
        """Return the value of one Yard (yd)
        based on a base imperial value"""
        return self.imperial_base * 36.0

    def unit_m(self):
        """Return the value of one Meter (m)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def unit_km(self):
        """Return the value of one Kilometer (km)
        based on a base metric value"""
        return self.metric_base * 1000000.0

    def unit_mi(self):
        """Return the value of one Mile (mi)
        based on a base imperial value"""
        return self.imperial_base * 63360.0


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
