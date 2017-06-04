"""placeholder docstring"""


class TimeUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.time_base = 1.0  # minutes in a minute

    def getunitval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def doconvert(self, ufrom, uto, amount):
        """
        Return calculated conversion between two units

        :param ufrom: unit to convert from, i.e. KB
        :param uto: unit to convert to, i.e. MB
        :param amount: amount to convert, i.e. 100
        :returns: original amount, converted amount, from unit, to unit,
         i.e. 100 kB is 0.1 MB
        """
        conversion = (amount * self.getunitval(ufrom)) / self.getunitval(uto)
        return "{0} {1} is {2} {3}".format(amount, ufrom, conversion, uto)

    def unit_ms(self):
        """Return the value of one Millisecond (ms)
        based on a base time value"""
        return (self.time_base / 1000.0) / 60.0

    def unit_sec(self):
        """Return the value of one Second (sec)
        based on a base time value"""
        return self.time_base / 60.0

    def unit_min(self):
        """Return the value of one Minute (min)
        based on a base time value"""
        return self.time_base

    def unit_hr(self):
        """Return the value of one Hour (hr)
        based on a base time value"""
        return self.time_base * 60.0

    def unit_day(self):
        """Return the value of one Day (day)
        based on a base time value"""
        return (self.time_base * 60.0) * 24.0

    def unit_wk(self):
        """Return the value of one Week (wk)
        based on a base time value"""
        return ((self.time_base * 60.0) * 24.0) * 7

    def unit_mo(self):
        """Return the value of one Month (mo)
        based on a base time value"""
        return (((self.time_base * 60.0) * 24.0) * 365.0) / 12

    def unit_yr(self):
        """Return the value of one Year (yr)
        based on a base time value"""
        return ((self.time_base * 60.0) * 24.0) * 365.0
