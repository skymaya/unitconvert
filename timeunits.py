class TimeUnit(object):
    def __init__(self):
        self.time_base = 1.0

    def getunitval(self, argument):
        """Dispatch method"""
        function = 'unit_'+str(argument)
        function = getattr(self, function, lambda: None)
        return function()

    def unit_ms(self):
        return self.time_base

    def unit_sec(self):
        return (self.time_base * 1000.0)

    def unit_min(self):
        return (self.time_base * 1000.0) * 60.0

    def unit_hr(self):
        return (self.time_base * 1000.0) * 3600.0

    def unit_day(self):
        return ((self.decimal_base * 1000.0) * 3600.0) * 24.0

    def unit_wk(self):
        return (((self.decimal_base * 1000) * 3600.0) * 24.0) * 7

    def unit_mo(self):
        return (((self.decimal_base * 1000) * 3600.0) * 365.0) / 12

    def unit_yr(self):
        return (((self.decimal_base * 1000) * 3600.0) * 24.0) * 365.0
