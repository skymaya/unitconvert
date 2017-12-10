# pylint: disable=I0011,R0903
"""
Module name: volumeunits

Calculate and return a value of one volume unit converted from another volume
unit.

Example:
    VolumeUnit(1, 'tbsp', 'tsp').doconvert()
    returns: 3.0

Exportables:
    Classes:
        VolumeUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""

from unitconvert.parentclasses import PositiveUnit


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
