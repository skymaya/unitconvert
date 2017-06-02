#!/usr/bin/python

"""docstring"""

from __future__ import print_function

#  standard library imports
#import sys
import argparse

# local application/library specific imports
from unitconvert.digitalunits import DigitalUnit
from unitconvert.lengthunits import LengthUnit
from unitconvert.timeunits import TimeUnit
from unitconvert.volumeunits import VolumeUnit

# abbr for microseconds is mus
TIME_UNITS = ['ms', 'sec', 'wk', 'day', 'hr', 'min', 'mo', 'yr']
DIGITAL_UNITS = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
LENGTH_UNITS = ['mm', 'cm', 'in', 'ft', 'yd', 'm', 'km', 'mi']
VOLUME_UNITS = ['ml', 'tsp', 'tbsp', 'cup', 'pt', 'qt', 'gal', 'l', 'in3', 'ft3']

def do_argparser():
    """Parse and return command line arguments"""
    parser = argparse.ArgumentParser(
        description='''
        A simple command-line unit conversion tool.
        ''',
        epilog='''Available unit types and units:
        Digital: B, kB, MB, GB, TB, PB, EB, ZB, YB
        Length: mm, cm, in, ft, yd, m, km, mi
        Time: ms, sec, min, hr, day, wk, mo, yr
        Volume: ml, tsp, tbsp, cup, pt, qt, gal, l, in3, ft3
        ''',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--amount', help='Amount to convert')
    parser.add_argument('-f', '--unit_from', help='Unit to convert from')
    parser.add_argument('-t', '--unit_to', help='Unit to convert to')
    return parser.parse_args()

def doconvert(ufrom, uto, amount, init):
    """Given a unit from, unit to convert to, amount to convert, and an
    instance that calculates the units' base value, return the converted
    amount"""
    conversion = (float(amount) * init.getunitval(ufrom)) / init.getunitval(uto)
    return "{0} {1} is {2} {3}".format(amount, ufrom, conversion, uto)

def main():
    """Main function"""
    args = do_argparser()

    if args.unit_from in DIGITAL_UNITS and args.unit_to in DIGITAL_UNITS:
        digiu = DigitalUnit()
        print(doconvert(args.unit_from, args.unit_to, args.amount, digiu))

    if args.unit_from in LENGTH_UNITS and args.unit_to in LENGTH_UNITS:
        lenu = LengthUnit()
        print(doconvert(args.unit_from, args.unit_to, args.amount, lenu))

    if args.unit_from in TIME_UNITS and args.unit_to in TIME_UNITS:
        timeu = TimeUnit()
        print(doconvert(args.unit_from, args.unit_to, args.amount, timeu))

    if args.unit_from in VOLUME_UNITS and args.unit_to in VOLUME_UNITS:
        volu = VolumeUnit()
        print(doconvert(args.unit_from, args.unit_to, args.amount, volu))

if __name__ == "__main__":
    main()
