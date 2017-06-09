#!/usr/bin/python

# pylint: skip-file


class TemperatureUnit(object):
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def getuval(self, argument):
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function)
        return function()

    def doconvert(self):
        print(self.getuval(self.ufrom))
        conv = self.getuval(self.ufrom)[self.uto]
        return "{0} {1} is {2} {3}".format(self.amt, self.ufrom, conv, self.uto)

    def unit_F(self):
        calc = {
            'C': (self.amt - 32.0) * 5 / 9,
            'K': (self.amt + 459.67) * 5 / 9,
            'F': self.amt
        }
        return calc

    def unit_C(self):
        calc = {
            'F': (self.amt * 9) / 5 + 32.0,
            'K': self.amt + 273.15,
            'C': self.amt
        }
        return calc

    def unit_K(self):
        if self.amt < 0:
            raise ValueError('Amount must be a positive number')
        calc = {
            'F': (self.amt * 9) / 5 - 459.67,
            'C': self.amt - 273.15,
            'K': self.amt
        }
        return calc


#print TemperatureUnit(2, 'K', 'F').doconvert()
print TemperatureUnit(2, 'K', 'F').unit_K()
print TemperatureUnit(2, 'K', 'F').unit_F()
print TemperatureUnit(2, 'K', 'F').unit_C()
