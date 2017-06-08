# pylint: disable=I0011,R0903
"""
Module name: volumeunits

Calculate and return a value of one volume unit converted from another volume
unit.

Example:
    VolumeUnit(1, 'tbsp', 'tsp').doconvert()
    returns: 1.0 tbsp is 3.0 tsp

Exportables:
    Classes:
        VolumeUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""


class VolumeUnit(object):
    """placeholder docstring"""
    def __init__(self, amt, ufrom, uto):
        self.metric_base = 1.0  # milliliters in a milliliter
        self.us_base = 4.92892159  # milliliters in a teaspoon
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def _getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = '_unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
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
        return "{0} {1} is {2} {3}".format(self.amt, self.ufrom, conv, self.uto)

    def _unit_ml(self):
        """Return the value of one Milliliter (ml)
        based on a base metric value"""
        return self.metric_base

    def _unit_tsp(self):
        """Return the value of one Teaspoon (tsp)
        based on a base us value"""
        return self.us_base

    def _unit_tbsp(self):
        """Return the value of one Tablespoon (tbsp)
        based on a base us value"""
        return self.us_base * 3.0

    def _unit_cup(self):
        """Return the value of one Cup (cup)
        based on a base us value"""
        return self.us_base * 48.0

    def _unit_pt(self):
        """Return the value of one Pint (pt)
        based on a base us value"""
        return self.us_base * 96.0

    def _unit_qt(self):
        """Return the value of one Quart (qt)
        based on a base us value"""
        return self.us_base * 192.0

    def _unit_gal(self):
        """Return the value of one Gallon (gal)
        based on a base us value"""
        return self.us_base * 768.0

    def _unit_l(self):
        """Return the value of one Liter (l)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def _unit_in3(self):
        """Return the value of one Cubic Inch (in3)
        based on a base us value"""
        return (self.us_base * 768.0) / 231

    def _unit_ft3(self):
        """Return the value of one Cubic Foot (ft3)
        based on a base us value"""
        return ((self.us_base * 768.0) / 231) * 1728
