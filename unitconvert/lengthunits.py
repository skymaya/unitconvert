# pylint: disable=I0011,R0903
"""
Module name: lengthunits

Calculate and return a value of one length unit converted from another length
unit.

Example:
    LengthUnit(1, 'ft', 'in').doconvert()
    returns: 1.0 ft is 12.0 in

Exportables:
    Classes:
        LengthUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""


class LengthUnit(object):
    """
    Initialize a LengthUnit to return the results of doconvert(), for the
    purpose of converting one length unit to another length unit

    :param amt: float, amount to convert from
    :param ufrom: string, unit to convert from
    :param uto: string, unit to convert to
    """
    def __init__(self, amt, ufrom, uto):
        self.imperial_base = 25.4000508001  # millimeters in an inch
        self.metric_base = 1.0  # millimeters in a millimeter
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def _getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = '_unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def doconvert(self):
        """
        Return calculated conversion between two units

        :returns: string containing original unit and value with converted
        unit and value
        :raises ValueError: if the amount (amt) is less than 0
        """
        if self.amt < 0:
            raise ValueError('Amount must be a positive number')
        conv = (self.amt * self._getuval(self.ufrom)) / self._getuval(self.uto)
        return "{0} {1} is {2} {3}".format(self.amt, self.ufrom, conv, self.uto)

    def _unit_mm(self):
        """Return the value of one Millimeter (mm)
        based on a base metric value"""
        return self.metric_base

    def _unit_cm(self):
        """Return the value of one Centimeter (cm)
        based on a base metric value"""
        return self.metric_base * 10.0

    def _unit_in(self):
        """Return the value of one Inch (in)
        based on a base imperial value"""
        return self.imperial_base

    def _unit_ft(self):
        """Return the value of one Foot (ft)
        based on a base imperial value"""
        return self.imperial_base * 12.0

    def _unit_yd(self):
        """Return the value of one Yard (yd)
        based on a base imperial value"""
        return self.imperial_base * 36.0

    def _unit_m(self):
        """Return the value of one Meter (m)
        based on a base metric value"""
        return self.metric_base * 1000.0

    def _unit_km(self):
        """Return the value of one Kilometer (km)
        based on a base metric value"""
        return self.metric_base * 1000000.0

    def _unit_mi(self):
        """Return the value of one Mile (mi)
        based on a base imperial value"""
        return self.imperial_base * 63360.0
