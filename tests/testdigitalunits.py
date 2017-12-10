#!/usr/bin/python

# pylint: disable=I0011,C0103,R0903,W0108

"""Unit tests for the digitalunits module"""

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


class DigitalUnit(PositiveUnit):
    """
    Initialize a DigitalUnit to return the results of doconvert(), for the
    purpose of converting one digital unit to another digital unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, *args, **kwargs):
        super(DigitalUnit, self).__init__(*args, **kwargs)
        self.dec_base = 1.0 # decimal base - bytes in a byte
        self.bin_base = 1.024 # binary base - bytes in a byte
        self.kb = self.dec_base * 1000.0 # kB base
        self.kib = self.bin_base * 1000.0 # KiB base

        self.units = {
            'B': self.dec_base,
            'kB': self.kb,
            'KiB': self.kib,
            'MB': self.kb ** 2,
            'MiB': self.kib ** 2,
            'GB': self.kb ** 3,
            'GiB': self.kib ** 3,
            'TB': self.kb ** 4,
            'TiB': self.kib ** 4,
            'PB': self.kb ** 5,
            'PiB': self.kib ** 5,
            'EB': self.kb ** 6,
            'EiB': self.kib ** 6,
            'ZB': self.kb ** 7,
            'ZiB': self.kib ** 7,
            'YB': self.kb ** 8,
            'YiB': self.kib ** 8
        }


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_mb2tb(self):
        """Test converting MB to TB"""
        result = round(DigitalUnit(326578, 'MB', 'TB').doconvert(), 3)
        self.assertEqual(result, round(0.326578, 3))

    def test_kib2mb(self):
        """Test converting KiB to MB"""
        result = round(DigitalUnit(26978, 'KiB', 'MB').doconvert(), 3)
        self.assertEqual(result, round(27.625472, 3))

    def test_gb2gib(self):
        """Test converting GB to GiB"""
        result = round(DigitalUnit(5, 'GB', 'GiB').doconvert(), 3)
        self.assertEqual(result, round(4.65661287308, 3))


class TestExceptions(unittest.TestCase):
    """Test cases to ensure providing a negative amount throws ValueError."""
    def test_mb2tb(self):
        """Test converting MB to TB"""
        result = DigitalUnit(-32, 'MB', 'TB')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_kib2mb(self):
        """Test converting KiB to MB"""
        result = DigitalUnit(-2, 'KiB', 'MB')
        self.assertRaises(ValueError, lambda: result.doconvert())

    def test_gb2gib(self):
        """Test converting GB to GiB"""
        result = DigitalUnit(-6, 'GB', 'GiB')
        self.assertRaises(ValueError, lambda: result.doconvert())


if __name__ == '__main__':
    unittest.main()
