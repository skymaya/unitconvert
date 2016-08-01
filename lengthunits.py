class LengthUnit(object):
    def __init__(self):
        self.imperial_base = 25.4000508001
        self.metric_base = 1.0
    def unit_base(self):
        if self.type == 'imperial':
            return self.imperial_base
        elif self.type == 'metric':
            return self.metric_base
        else:
            pass


class Millimeter(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.type = 'metric'


class Centimeter(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.metric_base = 10.0
        self.type = 'metric'


class Inch(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.type = 'imperial'


class Foot(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.imperial_base = self.imperial_base * 12.0
        self.type = 'imperial'


class Yard(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.imperial_base = self.imperial_base * 36.0
        self.type = 'imperial'


class Meter(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.metric_base = 1000.0
        self.type = 'metric'


class Kilometer(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.metric_base = 1000000.0
        self.type = 'metric'


class Mile(LengthUnit):
    def __init__(self):
        LengthUnit.__init__(self)
        self.imperial_base = self.imperial_base * 63360.0
        self.type = 'imperial'