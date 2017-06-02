"""placeholder docstring"""


class VolumeUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.metric_base = 1.0
        self.us_base = 4.92892159

    def getunitval(self, argument):
        """Takes a unit and returns a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_ml(self):
        """placeholder docstring"""
        return self.metric_base

    def unit_tsp(self):
        """placeholder docstring"""
        return self.us_base

    def unit_tbsp(self):
        """placeholder docstring"""
        return self.us_base * 3.0

    def unit_cup(self):
        """placeholder docstring"""
        return self.us_base * 48.0

    def unit_pt(self):
        """placeholder docstring"""
        return self.us_base * 96.0

    def unit_qt(self):
        """placeholder docstring"""
        return self.us_base * 192.0

    def unit_gal(self):
        """placeholder docstring"""
        return self.us_base * 768.0

    def unit_l(self):
        """placeholder docstring"""
        return self.metric_base * 1000.0

    def unit_in3(self):
        """placeholder docstring"""
        return (self.us_base * 768.0) / 231

    def unit_ft3(self):
        """placeholder docstring"""
        return ((self.us_base * 768.0) / 231) * 1728
