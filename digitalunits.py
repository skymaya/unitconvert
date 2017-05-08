class DigitalUnit(object):
    def __init__(self):
        self.decimal_base = 1.0
        self.binary_base = 1.024

    def getunitval(self, argument):
        """Takes a unit and returns a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_B(self):
        return self.decimal_base

    def unit_kB(self):
        return (self.decimal_base * 1000)

    def unit_MB(self):
        return (self.decimal_base * 1000) ** 2

    def unit_GB(self):
        return (self.decimal_base * 1000) ** 3

    def unit_TB(self):
        return (self.decimal_base * 1000) ** 4

    def unit_PB(self):
        return (self.decimal_base * 1000) ** 5

    def unit_EB(self):
        return (self.decimal_base * 1000) ** 6

    def unit_ZB(self):
        return (self.decimal_base * 1000) ** 7

    def unit_YB(self):
        return (self.decimal_base * 1000) ** 8
