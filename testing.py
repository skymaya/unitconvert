#!/usr/bin/env python

import traceback
import sys
import argparse
from digitalunits import (Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte,
Exabyte, Zettabyte, Yottabyte, createdigital)
from lengthunits import (Millimeter, Centimeter, Inch, Foot, Yard, Meter,
Kilometer, Mile, createlength)
from timeunits import (Millisecond, Second, Minute, Hour, Day, Week, Month,
Year, createtime)
from massunits import *

time_units = ['ms', 'sec', 'wk', 'day', 'hr', 'min', 'mo', 'yr']
digital_units = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
length_units = ['mm', 'cm', 'in', 'ft', 'yd', 'm', 'km', 'mi']

parser = argparse.ArgumentParser(description='''
    A simple command-line unit conversion tool.
    ''',
    epilog='''
    Available unit types and units:

    Digital: B, kB, MB, GB, TB, PB, EB, ZB, YB
    Length: mm, cm, in, ft, yd, m, km, mi
    Time: ms, sec, min, hr, day, wk, mo, yr
    ''', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-a', '--amount', help='Amount to convert')
parser.add_argument('-f', '--unit_from', help='Unit to convert from')
parser.add_argument('-t', '--unit_to', help='Unit to convert to')

args = parser.parse_args()

if args.unit_from in digital_units and args.unit_to in digital_units:
    conversion = (float(args.amount) * createdigital(args.unit_from)) / createdigital(args.unit_to)
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)

if args.unit_from in length_units and args.unit_to in length_units:
    conversion = (float(args.amount) * createlength(args.unit_from)) / createlength(args.unit_to)
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)

if args.unit_from in time_units and args.unit_to in time_units:
    conversion = (float(args.amount) * createtime(args.unit_from)) / createtime(args.unit_to)
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)
# else:
#     print 'Cannot convert to units of different types. Please see the help option (-h or --help) for usage information'
