class TimeUnit(object):
    def __init__(self):
        self.time_base = 1.0
    def unit_base(self):
        return self.time_base


class Millisecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)


class Second(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = 1000.0


class Minute(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = 1000.0 * 60.0


class Hour(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = 1000.0 * 3600.0


class Day(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = (1000.0 * 3600.0) * 24.0


class Week(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = ((1000.0 * 3600.0) * 24.0) * 7


class Month(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = ((1000.0 * 3600.0) * 365.0) / 12


class Year(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self)
        self.time_base = ((1000.0 * 3600.0) * 24.0) * 365.0


def createtime(unit):
    if unit == 'ms':
        unit = Millisecond().unit_base()
    if unit == 'sec':
        unit = Second().unit_base()
    if unit == 'min':
        unit = Minute().unit_base()
    if unit == 'hr':
        unit = Hour().unit_base()
    if unit == 'day':
        unit = Day().unit_base()
    if unit == 'wk':
        unit = Week().unit_base()
    if unit == 'mo':
        unit = Month().unit_base()
    if unit == 'yr':
        unit = Year().unit_base()
    return unit
