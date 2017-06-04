"""placeholder docstring"""


class MassUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.metric_base = 1.0  # grams in a gram
        self.imperial_base = 28.349523125  # grams in an ounce

    def getunitval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_mg(self):
        """Return the value of one Milligram (mg)
        based on a base metric value"""
        return self.metric_base / 1000.0

    def unit_g(self):
        """Return the value of one Gram (g)
        based on a base metric value"""
        return self.metric_base

    def unit_oz(self):
        """Return the value of one Ounce (oz)
        based on a base imperial value"""
        return self.imperial_base

    def unit_lb(self):
        """Return the value of one Pound (lb)
        based on a base imperial value"""
        return self.imperial_base * 16.0

    def unit_kg(self):
        """Return the value of one Kilogram (kg)
        based on a base metric value"""
        return self.metric_base * 1000.0
