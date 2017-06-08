# pylint: disable=I0011,C0103
"""
Module name: temperatureunits

Calculate and return a value of one temperature unit converted from another
temperature unit.

Example:
    TemperatureUnit(32, 'F', 'C').doconvert()
    returns: 32.0 F is 0.0 C

Classes:
    TemperatureUnit
        Functions:
            getuval
            doconvert
            unit_F
            unit_C
            unit_K
"""


class TemperatureUnit(object):
    """placeholder docstring"""
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def doconvert(self):
        """Return calculated conversion between two units"""
        conv = self.getuval(self.ufrom)[0][self.uto]
        return "{0} {1} is {2} {3}".format(self.amt, self.ufrom, conv, self.uto)

    def unit_F(self):
        """placeholder docstring"""
        calc = {
            'C': (self.amt - 32.0) * 5 / 9,
            'K': (self.amt + 459.67) * 5 / 9,
            'F': self.amt
        },
        return calc

    def unit_C(self):
        """placeholder docstring"""
        calc = {
            'F': (self.amt * 9) / 5 + 32.0,
            'K': self.amt + 273.15,
            'C': self.amt
        },
        return calc

    def unit_K(self):
        """placeholder docstring"""
        calc = {
            'F': self.amt * 9 / 5 - 459.67,
            'C': self.amt - 273.15,
            'K': self.amt
        }
        return calc
