#!/usr/bin/python

#  standard library imports
import sys
import argparse

# local application/library specific imports
from digitalunits import DigitalUnit
from lengthunits import LengthUnit
from timeunits import TimeUnit
# from massunits import *

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

def doconvert(ufrom, to, amount, init):
    conversion = (float(amount) * init.getunitval(ufrom)) / init.getunitval(to)
    return "{0} {1} is {2} {3}".format(amount, ufrom, conversion, to)

if args.unit_from in digital_units and args.unit_to in digital_units:
    du = DigitalUnit()
    print doconvert(args.unit_from, args.unit_to, args.amount, du)

if args.unit_from in length_units and args.unit_to in length_units:
    lu = LengthUnit()
    print doconvert(args.unit_from, args.unit_to, args.amount, lu)

if args.unit_from in time_units and args.unit_to in time_units:
    tu = TimeUnit()
    print doconvert(args.unit_from, args.unit_to, args.amount, tu)
