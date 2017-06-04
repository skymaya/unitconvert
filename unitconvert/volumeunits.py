"""placeholder docstring"""


class VolumeUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.metric_base = 1.0  # milliliters in a milliliter
        self.us_base = 4.92892159  # milliliters in a teaspoon

    def getunitval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def unit_ml(self):
        """Return the value of one Milliliter (ml)
        based on a base metric value"""
        return self.metric_base

    def unit_tsp(self):
        """Return the value of one Teaspoon (tsp)
        based on a base us value"""
        return self.us_base

    def unit_tbsp(self):
        """Return the value of one Tablespoon (tbsp)
        based on a base us value"""
        return self.us_base * 3.0

    def unit_cup(self):
        """Return the value of one Cup (cup)
        based on a base us value"""
        return self.us_base * 48.0

    def unit_pt(self):
        """Return the value of one Pint (pt)
        based on a base us value"""
        return self.us_base * 96.0

    def unit_qt(self):
        """Return the value of one Quart (qt)
        based on a base us value"""
        return self.us_base * 192.0

    def unit_gal(self):
        """Return the value of one Gallon (gal)
        based on a base us value"""
        return self.us_base * 768.0

    def unit_l(self):
        """Return the value of one Liter (l)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def unit_in3(self):
        """Return the value of one Cubic Inch (in3)
        based on a base us value"""
        return (self.us_base * 768.0) / 231

    def unit_ft3(self):
        """Return the value of one Cubic Foot (ft3)
        based on a base us value"""
        return ((self.us_base * 768.0) / 231) * 1728
