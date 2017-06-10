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


class MassUnit(object):
    """
    Initialize a MassUnit to return the results of doconvert(), for the
    purpose of converting one mass unit to another mass unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.metric_base = 1.0  # grams in a gram
        self.imperial_base = 28.349523125  # grams in an ounce
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def _getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = '_unit_{0}'.format(str(argument))
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
        conv = (self.amt * self._getuval(self.ufrom)) / self._getuval(self.uto)
        return conv

    def _unit_mg(self):
        """Return the value of one Milligram (mg)
        based on a base metric value"""
        return self.metric_base / 1000.0

    def _unit_g(self):
        """Return the value of one Gram (g)
        based on a base metric value"""
        return self.metric_base

    def _unit_oz(self):
        """Return the value of one Ounce (oz)
        based on a base imperial value"""
        return self.imperial_base

    def _unit_lb(self):
        """Return the value of one Pound (lb)
        based on a base imperial value"""
        return self.imperial_base * 16.0

    def _unit_kg(self):
        """Return the value of one Kilogram (kg)
        based on a base metric value"""
        return self.metric_base * 1000.0
