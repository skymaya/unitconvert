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


class VolumeUnit(object):
    """
    Initialize a VolumeUnit to return the results of doconvert(), for the
    purpose of converting one volume unit to another volume unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.metric_base = 1.0  # milliliters in a milliliter
        self.us_customary_base = 4.92892159375  # milliliters in a teaspoon
        self.us_legal_base = 5.0  # milliliters in a teaspoon
        self.imperial_base = 5.916666666666667  # milliliters in a teaspoon
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

    def _unit_ml(self):
        """Return the value of one Milliliter (ml)
        based on a base metric value"""
        return self.metric_base

    def _unit_tsp(self):
        """Return the value of one Teaspoon (tsp)
        based on a base us customary value"""
        return self.us_customary_base

    def _unit_tbsp(self):
        """Return the value of one Tablespoon (tbsp)
        based on a base us customary value"""
        return self.us_customary_base * 3.0

    def _unit_floz(self):
        """Return the value of one US customary fluid Ounce (floz)
        based on a base us customary value"""
        return self.us_customary_base * 6.0

    def _unit_cup(self):
        """Return the value of one US customary Cup (cup)
        based on a base us customary value"""
        return self.us_customary_base * 48.0

    def _unit_lcup(self):
        """Return the value of one US legal Cup (lcup)
        based on a base us legal value"""
        return self.us_legal_base * 48.0

    def _unit_pt(self):
        """Return the value of one Pint (pt)
        based on a base us customary value"""
        return self.us_customary_base * 96.0

    def _unit_qt(self):
        """Return the value of one Quart (qt)
        based on a base us customary value"""
        return self.us_customary_base * 192.0

    def _unit_gal(self):
        """Return the value of one Gallon (gal)
        based on a base us customary value"""
        return self.us_customary_base * 768.0

    def _unit_l(self):
        """Return the value of one Liter (l)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def _unit_in3(self):
        """Return the value of one Cubic Inch (in3)
        based on a base us customary value"""
        return (self.us_customary_base * 768.0) / 231

    def _unit_ft3(self):
        """Return the value of one Cubic Foot (ft3)
        based on a base us customary value"""
        return ((self.us_customary_base * 768.0) / 231) * 1728
