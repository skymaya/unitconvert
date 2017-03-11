class DigitalUnit(object):
    def __init__(self):
        self.decimal_base = 1000.0
        self.binary_base = 1024.0
    def unit_base(self):
        if self.type == 'decimal':
            return self.decimal_base
        elif self.type == 'binary':
            return self.binary_base
        else:
            pass


class Byte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = 1.0
        self.type = 'decimal'


class Kilobyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base
        self.type = 'decimal'


class Megabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**2
        self.type = 'decimal'


class Gigabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**3
        self.type = 'decimal'


class Terabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**4
        self.type = 'decimal'


class Petabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**5
        self.type = 'decimal'


class Exabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**6
        self.type = 'decimal'


class Zettabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**7
        self.type = 'decimal'


class Yottabyte(DigitalUnit):
    def __init__(self):
        DigitalUnit.__init__(self)
        self.decimal_base = self.decimal_base**8
        self.type = 'decimal'


def createdigital(unit):
    if unit == 'B':
        unit = Byte().unit_base()
    if unit == 'kB':
        unit = Kilobyte().unit_base()
    if unit == 'MB':
        unit = Megabyte().unit_base()
    if unit == 'GB':
        unit = Gigabyte().unit_base()
    if unit == 'TB':
        unit = Terabyte().unit_base()
    if unit == 'PB':
        unit = Petabyte().unit_base()
    if unit == 'EB':
        unit = Exabyte().unit_base()
    if unit == 'ZB':
        unit = Zettabyte().unit_base()
    if unit == 'YB':
        unit = Yottabyte().unit_base()
    return unit
