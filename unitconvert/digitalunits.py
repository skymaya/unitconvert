# pylint: disable=I0011,C0103,R0903
"""
Module name: digitalunits

Calculate and return a value of one digital unit converted from another digital
unit.

Example:
    DigitalUnit(5, 'GB', 'MB').doconvert()
    returns: 5000.0

Exportables:
    Classes:
        DigitalUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""

from unitconvert.parentclasses import PositiveUnit


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
