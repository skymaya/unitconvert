#!/usr/bin/python

# pylint: disable=I0011,W0108,R0903

"""Unit tests for the timeunits module"""

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


class TimeUnit(PositiveUnit):
    """
    Initialize a TimeUnit to return the results of doconvert(), for the
    purpose of converting one time unit to another time unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, *args, **kwargs):
        super(TimeUnit, self).__init__(*args, **kwargs)

        self.units = {
            'ms': (1.0 / 1000.0) / 60.0,
            'sec': 1.0 / 60.0,
            'min': 1.0, # base - minutes in a minute
            'hr': 60.0,
            'day': 60.0 * 24.0,
            'wk': (60.0 * 24.0) * 7,
            'mo': ((60.0 * 24.0) * 365.0) / 12,
            'yr': (60.0 * 24.0) * 365.0
        }


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
