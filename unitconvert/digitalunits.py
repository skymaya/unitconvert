# pylint: disable=I0011,C0103

"""placeholder docstring"""


class DigitalUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.decimal_base = 1.0
        self.binary_base = 1.024

    def getunitval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_B(self):
        """Return the value of one Byte (B)
        based on a base decimal value"""
        return self.decimal_base

    def unit_kB(self):
        """Return the value of one Kilobyte (kB)
        based on a base decimal value"""
        return self.decimal_base * 1000

    def unit_MB(self):
        """Return the value of one Megabyte (MB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 2

    def unit_GB(self):
        """Return the value of one Gigabyte (GB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 3

    def unit_TB(self):
        """Return the value of one Terabyte (TB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 4

    def unit_PB(self):
        """Return the value of one Petabyte (PB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 5

    def unit_EB(self):
        """Return the value of one Exabyte (EB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 6

    def unit_ZB(self):
        """Return the value of one Zettabyte (ZB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 7

    def unit_YB(self):
        """Return the value of one Yottabyte (YB)
        based on a base decimal value"""
        return (self.decimal_base * 1000) ** 8
