#!/usr/bin/env python

import traceback
import sys
import argparse
from digitalunits import *
from lengthunits import *
from timeunits import *
from massunits import *


# create digital instances
byte = Byte().unit_base()
kilobyte = Kilobyte().unit_base()
megabyte = Megabyte().unit_base()
gigabyte = Gigabyte().unit_base()
terabyte = Terabyte().unit_base()
petabyte = Petabyte().unit_base()
exabyte = Exabyte().unit_base()
zettabyte = Zettabyte().unit_base()
yottabyte = Yottabyte().unit_base()

# create length instances
millimeter = Millimeter().unit_base()
centimeter = Centimeter().unit_base()
inch = Inch().unit_base()
foot = Foot().unit_base()
yard = Yard().unit_base()
meter = Meter().unit_base()
kilometer = Kilometer().unit_base()
mile = Mile().unit_base()

# create length instances
millisecond = Millisecond().unit_base()
second = Second().unit_base()
minute = Minute().unit_base()
hour = Hour().unit_base()
day = Day().unit_base()
week = Week().unit_base()
month = Month().unit_base()
year = Year().unit_base()

# associate user input unit abbreviations with time instances
time_units = {
    'ms': millisecond,
    'sec': second,
    'wk': week,
    'day': day,
    'hr': hour,
    'min': minute,
    'mo': month,
    'yr': year
}

# associate user input unit abbreviations with digital instances
digital_units = {
    'B': byte,
    'kB': kilobyte,
    'MB': megabyte,
    'GB': gigabyte,
    'TB': terabyte,
    'PB': petabyte,
    'EB': exabyte,
    'ZB': zettabyte,
    'YB': yottabyte
}

# associate user input unit abbreviations with length instances
length_units = {
    'mm': millimeter,
    'cm': centimeter,
    'in': inch,
    'ft': foot,
    'yd': yard,
    'm': meter,
    'km': kilometer,
    'mi': mile
}

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
    conversion = (float(args.amount) * digital_units[args.unit_from]) / digital_units[args.unit_to]
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)

if args.unit_from in length_units and args.unit_to in length_units:
    conversion = (float(args.amount) * length_units[args.unit_from]) / length_units[args.unit_to]
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)

if args.unit_from in time_units and args.unit_to in time_units:
    conversion = (float(args.amount) * time_units[args.unit_from]) / time_units[args.unit_to]
    print "{0} {1} is {2} {3}".format(args.amount, args.unit_from, conversion, args.unit_to)
# else:
#     print 'Cannot convert to units of different types. Please see the help option (-h or --help) for usage information'
