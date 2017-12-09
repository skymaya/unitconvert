# pylint: disable=I0011,R0903
"""
Module name: lengthunits

Calculate and return a value of one length unit converted from another length
unit.

Example:
    LengthUnit(1, 'ft', 'in').doconvert()
    returns: 12.0

Exportables:
    Classes:
        LengthUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""

from unitconvert.parentclasses import PositiveUnit


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
