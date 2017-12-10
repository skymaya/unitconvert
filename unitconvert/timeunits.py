# pylint: disable=I0011,R0903
"""
Module name: timeunits

Calculate and return a value of one time unit converted from another time unit.

Example:
    TimeUnit(1, 'min', 'sec').doconvert()
    returns: 60.0

Exportables:
    Classes:
        TimeUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""

from unitconvert.parentclasses import PositiveUnit


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
