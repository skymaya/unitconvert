class LengthUnit(object):
    def __init__(self):
        self.imperial_base = 25.4000508001
        self.metric_base = 1.0

    def getunitval(self, argument):
        """Dispatch method"""
        function = 'unit_'+str(argument)
        function = getattr(self, function, lambda: None)
        return function()

    def unit_mm(self):
        return self.metric_base

    def unit_cm(self):
        return (self.metric_base * 10.0)

    def unit_in(self):
        return self.imperial_base

    def unit_ft(self):
        return (self.imperial_base * 12.0)

    def unit_yd(self):
        return (self.imperial_base * 36.0)

    def unit_m(self):
        return (self.metric_base * 1000.0)

    def unit_km(self):
        return (self.metric_base * 1000000.0)

    def unit_mi(self):
        return (self.imperial_base * 63360.0)
