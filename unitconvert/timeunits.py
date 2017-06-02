"""placeholder docstring"""

class TimeUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.time_base = 1.0

    def getunitval(self, argument):
        """Takes a unit and returns a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_ms(self):
        """placeholder docstring"""
        return self.time_base

    def unit_sec(self):
        """placeholder docstring"""
        return self.time_base * 1000.0

    def unit_min(self):
        """placeholder docstring"""
        return (self.time_base * 1000.0) * 60.0

    def unit_hr(self):
        """placeholder docstring"""
        return (self.time_base * 1000.0) * 3600.0

    def unit_day(self):
        """placeholder docstring"""
        return ((self.time_base * 1000.0) * 3600.0) * 24.0

    def unit_wk(self):
        """placeholder docstring"""
        return (((self.time_base * 1000) * 3600.0) * 24.0) * 7

    def unit_mo(self):
        """placeholder docstring"""
        return (((self.time_base * 1000) * 3600.0) * 365.0) / 12

    def unit_yr(self):
        """placeholder docstring"""
        return (((self.time_base * 1000) * 3600.0) * 24.0) * 365.0
