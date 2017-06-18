#!/usr/bin/python

"""
Module name: runconvert

This module contains the main function and arguments for the unitconvert
application.

Example:
    python runconvert.py -a 1 -f ft -t in
    returns: 1.0 ft is 12.0 in

Imports:
    argparse: standard library
    DigitalUnit from unitconvert.digitalunits: local application
    LengthUnit from unitconvert.lengthunits: local application
    TimeUnit from unitconvert.timeunits: local application
    VolumeUnit from unitconvert.volumeunits: local application
    MassUnit from unitconvert.massunits: local application
    TemperatureUnit from unitconvert.temperatureunits: local application

Functions:
    do_argparser: Parse and return command line arguments
    main: Main function

Constants:
    TIME_UNITS: list of time unit abbreviations
    DIGITAL_UNITS: list of digital unit abbreviations
    LENGTH_UNITS: list of length unit abbreviations
    VOLUME_UNITS: list of volume unit abbreviations
    MASS_UNITS: list of mass unit abbreviations
    TEMP_UNITS: list of temperature unit abbreviations
"""

from __future__ import print_function

#  standard library imports
import argparse

# local application/library specific imports
from unitconvert.digitalunits import DigitalUnit
from unitconvert.lengthunits import LengthUnit
from unitconvert.timeunits import TimeUnit
from unitconvert.volumeunits import VolumeUnit
from unitconvert.massunits import MassUnit
from unitconvert.temperatureunits import TemperatureUnit

# abbr for microseconds is mus
TIME_UNITS = ['ms', 'sec', 'wk', 'day', 'hr', 'min', 'mo', 'yr']
DIGITAL_UNITS = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'KiB',
                 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
LENGTH_UNITS = ['mm', 'cm', 'in', 'ft', 'yd', 'm', 'km', 'mi']
VOLUME_UNITS = ['ml', 'tsp', 'tbsp', 'cup', 'lcup', 'pt', 'qt', 'gal', 'l',
                'in3', 'ft3', 'floz']
MASS_UNITS = ['mg', 'g', 'oz', 'lb', 'kg']
TEMP_UNITS = ['F', 'C', 'K']

def do_argparser():
    """Parse and return command line arguments"""
    parser = argparse.ArgumentParser(
        description='''
        A simple command-line unit conversion tool.
        ''',
        epilog='''Available unit types and unit arguments:
Digital:
        Decimal: B, kB, MB, GB, TB, PB, EB, ZB, YB
        Binary: KiB, MiB, GiB, TiB, PiB, EiB, ZiB, YiB
Length: mm, cm, in, ft, yd, m, km, mi
Time: ms, sec, min, hr, day, wk, mo, yr
Volume:
        Metric: ml, l
        US customary: tsp, tbsp, floz, cup, pt, qt, gal
        US legal: lcup
        Cubic: in3, ft3
Mass: mg, g, oz, lb, kg
Temperature: F, C, K
        ''',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--amount', type=float, help='Amount to convert',
                        required=True)
    parser.add_argument('-f', '--unit_from', help='Unit to convert from',
                        required=True)
    parser.add_argument('-t', '--unit_to', help='Unit to convert to',
                        required=True)
    parser.add_argument('-v', '--version', help='unitconvert, Version 1.0.1, 2016-2017',
                        required=False)
    return parser.parse_args()

def format_output(org_amt, conv_amt, org_ufrom, conv_uto):
    """Return a string containing the original amount, original unit,
    converted amount, and unit converted to in a nice easy to read format."""
    return '{0} {1} is {2} {3}'.format(org_amt, org_ufrom, conv_amt, conv_uto)

def main():
    """Main function"""
    args = do_argparser()
    ufrom = args.unit_from
    uto = args.unit_to
    amt = args.amount

    if ufrom in DIGITAL_UNITS and uto in DIGITAL_UNITS:
        result = DigitalUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

    if ufrom in LENGTH_UNITS and uto in LENGTH_UNITS:
        result = LengthUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

    if ufrom in TIME_UNITS and uto in TIME_UNITS:
        result = TimeUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

    if ufrom in VOLUME_UNITS and uto in VOLUME_UNITS:
        result = VolumeUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

    if ufrom in MASS_UNITS and uto in MASS_UNITS:
        result = MassUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

    if ufrom in TEMP_UNITS and uto in TEMP_UNITS:
        result = TemperatureUnit(amt, ufrom, uto).doconvert()
        print(format_output(amt, result, ufrom, uto))

if __name__ == "__main__":
    main()
