#!/usr/bin/python

"""
Module name: runconvert

This module contains the main function for the unitconvert application.

example code to run module

List of classes
List of functions in the classes
List of imported modules
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
VOLUME_UNITS = ['ml', 'tsp', 'tbsp', 'cup', 'pt', 'qt', 'gal', 'l', 'in3', 'ft3']
MASS_UNITS = ['mg', 'g', 'oz', 'lb', 'kg']
TEMP_UNITS = ['F', 'C', 'K']

def do_argparser():
    """Parse and return command line arguments"""
    parser = argparse.ArgumentParser(
        description='''
        A simple command-line unit conversion tool.
        ''',
        epilog='''Available unit types and units:
        Digital:
                Decimal: B, kB, MB, GB, TB, PB, EB, ZB, YB
                Binary: KiB, MiB, GiB, TiB, PiB, EiB, ZiB, YiB
        Length: mm, cm, in, ft, yd, m, km, mi
        Time: ms, sec, min, hr, day, wk, mo, yr
        Volume: ml, tsp, tbsp, cup, pt, qt, gal, l, in3, ft3
        Mass: mg, g, oz, lb, kg
        Temperature: F, C, K
        ''',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--amount', type=float, help='Amount to convert')
    parser.add_argument('-f', '--unit_from', help='Unit to convert from')
    parser.add_argument('-t', '--unit_to', help='Unit to convert to')
    return parser.parse_args()

def main():
    """Main function"""
    args = do_argparser()
    ufrom = args.unit_from
    uto = args.unit_to
    amt = args.amount

    if ufrom in DIGITAL_UNITS and uto in DIGITAL_UNITS:
        print(DigitalUnit(amt, ufrom, uto).doconvert())

    if ufrom in LENGTH_UNITS and uto in LENGTH_UNITS:
        print(LengthUnit(amt, ufrom, uto).doconvert())

    if ufrom in TIME_UNITS and uto in TIME_UNITS:
        print(TimeUnit(amt, ufrom, uto).doconvert())

    if ufrom in VOLUME_UNITS and uto in VOLUME_UNITS:
        print(VolumeUnit(amt, ufrom, uto).doconvert())

    if ufrom in MASS_UNITS and uto in MASS_UNITS:
        print(MassUnit(amt, ufrom, uto).doconvert())

    if ufrom in TEMP_UNITS and uto in TEMP_UNITS:
        print(TemperatureUnit(amt, ufrom, uto).doconvert())

if __name__ == "__main__":
    main()
