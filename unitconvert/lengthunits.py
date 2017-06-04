"""placeholder docstring"""


class LengthUnit(object):
    """placeholder docstring"""
    def __init__(self):
        self.imperial_base = 25.4000508001  # millimeters in an inch
        self.metric_base = 1.0  # millimeters in a millimeter

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

    def unit_mm(self):
        """Return the value of one Millimeter (mm)
        based on a base metric value"""
        return self.metric_base

    def unit_cm(self):
        """Return the value of one Centimeter (cm)
        based on a base metric value"""
        return self.metric_base * 10.0

    def unit_in(self):
        """Return the value of one Inch (in)
        based on a base imperial value"""
        return self.imperial_base

    def unit_ft(self):
        """Return the value of one Foot (ft)
        based on a base imperial value"""
        return self.imperial_base * 12.0

    def unit_yd(self):
        """Return the value of one Yard (yd)
        based on a base imperial value"""
        return self.imperial_base * 36.0

    def unit_m(self):
        """Return the value of one Meter (m)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def unit_km(self):
        """Return the value of one Kilometer (km)
        based on a base metric value"""
        return self.metric_base * 1000000.0

    def unit_mi(self):
        """Return the value of one Mile (mi)
        based on a base imperial value"""
        return self.imperial_base * 63360.0
