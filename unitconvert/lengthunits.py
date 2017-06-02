"""placeholder docstring"""

class LengthUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.imperial_base = 25.4000508001
        self.metric_base = 1.0

    def getunitval(self, argument):
        """Takes a unit and returns a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_mm(self):
        """placeholder docstring"""
        return self.metric_base

    def unit_cm(self):
        """placeholder docstring"""
        return self.metric_base * 10.0

    def unit_in(self):
        """placeholder docstring"""
        return self.imperial_base

    def unit_ft(self):
        """placeholder docstring"""
        return self.imperial_base * 12.0

    def unit_yd(self):
        """placeholder docstring"""
        return self.imperial_base * 36.0

    def unit_m(self):
        """placeholder docstring"""
        return self.metric_base * 1000.0

    def unit_km(self):
        """placeholder docstring"""
        return self.metric_base * 1000000.0

    def unit_mi(self):
        """placeholder docstring"""
        return self.imperial_base * 63360.0
