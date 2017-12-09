# pylint: disable=I0011,R0903
"""
Module name: massunits

Calculate and return a value of one mass unit converted from another mass unit.

Example:
    MassUnit(16, 'oz', 'lb').doconvert()
    returns: 1.0

Exportables:
    Classes:
        MassUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""

from unitconvert.parentclasses import PositiveUnit

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
