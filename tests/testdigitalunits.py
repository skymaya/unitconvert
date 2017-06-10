#!/usr/bin/python

# pylint: disable=I0011,C0103,R0903

"""Unit tests for the digitalunits module"""

#  standard library imports
import unittest


class DigitalUnit(object):
    """
    Initialize a DigitalUnit to return the results of doconvert(), for the
    purpose of converting one digital unit to another digital unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.decimal_base = 1.0  # bytes in a byte (decimal)
        self.binary_base = 1.024 # bytes in a byte (binary)
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
        return "{0}".format(conv)

    def unit_B(self):
        """Return the value of one Byte (B)
        based on a base decimal value"""
        return self.decimal_base

    def unit_kB(self):
        """Return the value of one Kilobyte (kB)
        based on a base decimal value"""
        return self.decimal_base * 1000

    def unit_KiB(self):
        """Return the value of one Kibibyte (KiB)
        based on a base binary value"""
        return self.binary_base * 1000

    def unit_MB(self):
        """Return the value of one Megabyte (MB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 2

    def unit_MiB(self):
        """Return the value of one Mebibyte (MiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 2

    def unit_GB(self):
        """Return the value of one Gigabyte (GB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 3

    def unit_GiB(self):
        """Return the value of one Gibibyte (GiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 3

    def unit_TB(self):
        """Return the value of one Terabyte (TB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 4

    def unit_TiB(self):
        """Return the value of one Tebibyte (TiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 4

    def unit_PB(self):
        """Return the value of one Petabyte (PB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 5

    def unit_PiB(self):
        """Return the value of one Pebibyte (PiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 5

    def unit_EB(self):
        """Return the value of one Exabyte (EB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 6

    def unit_EiB(self):
        """Return the value of one Exbibyte (EiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 6

    def unit_ZB(self):
        """Return the value of one Zettabyte (ZB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 7

    def unit_ZiB(self):
        """Return the value of one Zebibyte (ZiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 7

    def unit_YB(self):
        """Return the value of one Yottabyte (YB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 8

    def unit_YiB(self):
        """Return the value of one Yobibyte (YiB)
        based on a base binary value"""
        return (self.binary_base * 1000) ** 8


class TestConversions(unittest.TestCase):
    """Test cases to ensure results are correct using a small sampling."""
    def test_mb2tb(self):
        """Test converting MB to TB"""
        result = DigitalUnit(326578, 'MB', 'TB').doconvert()
        self.assertEqual(result, '0.326578')

    def test_kib2mb(self):
        """Test converting KiB to MB"""
        result = DigitalUnit(26978, 'KiB', 'MB').doconvert()
        self.assertEqual(result, '27.625472')

    def test_gb2gib(self):
        """Test converting GB to GiB"""
        result = DigitalUnit(5, 'GB', 'GiB').doconvert()
        self.assertEqual(result, '4.65661287308')


if __name__ == '__main__':
    unittest.main()
