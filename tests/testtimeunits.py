#!/usr/bin/python

# pylint: disable=I0011,W0108

"""Unit tests for the timeunits module"""

#  standard library imports
import unittest


class TimeUnit(object):
    """
    Initialize a TimeUnit to return the results of doconvert(), for the
    purpose of converting one time unit to another time unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.time_base = 1.0  # minutes in a minute
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

    def unit_ms(self):
        """Return the value of one Millisecond (ms)
        based on a base time value"""
        return (self.time_base / 1000.0) / 60.0

    def unit_sec(self):
        """Return the value of one Second (sec)
        based on a base time value"""
        return self.time_base / 60.0

    def unit_min(self):
        """Return the value of one Minute (min)
        based on a base time value"""
        return self.time_base

    def unit_hr(self):
        """Return the value of one Hour (hr)
        based on a base time value"""
        return self.time_base * 60.0

    def unit_day(self):
        """Return the value of one Day (day)
        based on a base time value"""
        return (self.time_base * 60.0) * 24.0

    def unit_wk(self):
        """Return the value of one Week (wk)
        based on a base time value"""
        return ((self.time_base * 60.0) * 24.0) * 7

    def unit_mo(self):
        """Return the value of one Month (mo)
        based on a base time value"""
        return (((self.time_base * 60.0) * 24.0) * 365.0) / 12

    def unit_yr(self):
        """Return the value of one Year (yr)
        based on a base time value"""
        return ((self.time_base * 60.0) * 24.0) * 365.0


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_wk2yr(self):
        """Test converting wk to yr"""
        result = round(TimeUnit(34, 'wk', 'yr').doconvert(), 2)
        self.assertEqual(result, round(0.652055, 2))

    def test_hr2sec(self):
        """Test converting hr to sec"""
        result = round(TimeUnit(1.7, 'hr', 'sec').doconvert(), 2)
        self.assertEqual(result, round(6120.0, 2))

    def test_ms2min(self):
        """Test converting ft to in"""
        result = round(TimeUnit(50, 'ms', 'min').doconvert(), 4)
        self.assertEqual(result, round(0.000833333, 4))


class TestExceptions(unittest.TestCase):
    """Test cases to ensure providing a negative amount throws ValueError."""
    def test_wk2yr(self):
        """Test converting wk to yr"""
        result = TimeUnit(-34, 'wk', 'yr')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_hr2sec(self):
        """Test converting hr to sec"""
        result = TimeUnit(-1.7, 'hr', 'sec')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_ms2min(self):
        """Test converting ft to in"""
        result = TimeUnit(-50, 'ms', 'min')
        self.assertRaises(ValueError, lambda: result.doconvert())


if __name__ == '__main__':
    unittest.main()
