class Length(object):
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


class Millimeter(Length):
    def __init__(self):
        Length.__init__(self)
        self.type = 'metric'


class Centimeter(Length):
    def __init__(self):
        Length.__init__(self)
        self.metric_base = 10.0
        self.type = 'metric'


class Inch(Length):
    def __init__(self):
        Length.__init__(self)
        self.type = 'imperial'


class Foot(Length):
    def __init__(self):
        Length.__init__(self)
        self.imperial_base = self.imperial_base * 12.0
        self.type = 'imperial'


class Yard(Length):
    def __init__(self):
        Length.__init__(self)
        self.imperial_base = self.imperial_base * 36.0
        self.type = 'imperial'


class Meter(Length):
    def __init__(self):
        Length.__init__(self)
        self.metric_base = 1000.0
        self.type = 'metric'


class Kilometer(Length):
    def __init__(self):
        Length.__init__(self)
        self.metric_base = 1000000.0
        self.type = 'metric'


class Mile(Length):
    def __init__(self):
        Length.__init__(self)
        self.imperial_base = self.imperial_base * 63360.0
        self.type = 'imperial'