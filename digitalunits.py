class Digital(object):
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


class Byte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = 1.0
        self.type = 'decimal'


class Kilobyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base
        self.type = 'decimal'


class Megabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**2
        self.type = 'decimal'


class Gigabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**3
        self.type = 'decimal'


class Terabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**4
        self.type = 'decimal'


class Petabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**5
        self.type = 'decimal'


class Exabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**6
        self.type = 'decimal'


class Zettabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**7
        self.type = 'decimal'


class Yottabyte(Digital):
    def __init__(self):
        Digital.__init__(self)
        self.decimal_base = self.decimal_base**8
        self.type = 'decimal'