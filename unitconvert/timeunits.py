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
