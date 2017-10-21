# Unitconvert: Unit conversion tool - Version 1.0.3

## Synopsis

A command line tool and import library for performing unit conversions.

## Testing

There is a "tests" directory containing some unit tests for some of the classes and functions in this application.

Additionally, the application has been tested on the following systems and python versions:

* Ubuntu 16.04 (python 3.5.2, python 2.7.12)

## Known Issues

* Fully untested on Windows, Mac, and BSD at this time

## Installation

Install with pip:

`pip install unitconvert`

## Usage

After installation is completed, you may run the unitconvert tool in a terminal using the following command:

`unitconvert -a AMOUNT -f UNIT_FROM -t UNIT_TO`

To print version information:

`unitconvert -v`

To print help:

`unitconvert -h`

The unit libraries may also be imported and used in Python scripts to perform conversions. Example:

```
# Filename: testconvert.py
from unitconvert import digitalunits
print(digitalunits.DigitalUnit(500, 'GB', 'MB').doconvert())
```

Output:

```
$ python testconvert.py
500000.0
```

Command line arguments:
* -a AMOUNT: Amount to convert
* -f UNIT_FROM: Unit to convert from
* -t UNIT_TO: Unit to convert to
* -v VERSION: Optional, print version info
* -h with no other arguments: print help info

Available unit types with associated class (in brackets) and arguments (in parentheses):

* Digital [DigitalUnit]:
  - Decimal: Byte (B), Kilobyte (kB), Megabyte (MB), Gigabyte (GB), Terabyte (TB), Petabyte (PB), Exabyte (EB), Zettabyte (ZB), Yottabyte (YB)
  - Binary: Kibibyte (KiB), Mebibyte (MiB), Gibibyte (GiB), Tebibyte (TiB), Pebibyte (PiB), Exbibyte (EiB), Zebibyte (ZiB), Yobibyte (YiB)
* Length [LengthUnit]: Millimeter (mm), Centimeter (cm), Inch (in), Foot (ft), Yard (yd), Meter (m), Kilometer (km), Mile (mi)
* Time [TimeUnit]: Millisecond (ms), second (sec), Minute (min), Hour (hr), Day (day), Week (wk), Month (mo), Year (yr)
* Volume [VolumeUnit]:
  - Metric: Milliliter (ml), Liter (l)
  - US customary: Teaspoon (tsp), Tablespoon (tbsp), fluid Ounces (floz), Cup (cup), Pint (pt), Quart (qt), Gallon (gal)
  - US legal: Cup (lcup)
  - Cubic: Cubic Inch (in3), Cubic Foot (ft3)
* Mass [MassUnit]: Milligram (mg), Gram (g), Ounce (oz), Pound (lb), Kilogram (kg)
* Temperature [TemperatureUnit]: Fahrenheit (F), Celsius (C), Kelvin (K)

## Updating

If you want to update the application currently installed, just run the following to upgrade with pip:

`pip install unitconvert --upgrade`

## Uninstalling

If you want to uninstall the application, run the following to uninstall with pip:

`pip uninstall unitconvert`

## To Do

* Add support for more units

## Contributors

Get in touch with me if you'd like to contribute.

## License

The code contained within this repository is released under the MIT license.

## Changelog

### Version 1.0.3
* 10/21/2017: Updated README with import instructions. Updated setup.py and runconvert.py with updated description.

### Version 1.0.2
* 10/21/2017: Updated README

### Version 1.0.1
* 06/17/2017: Added fluid ounces

### Version 1.0.0
* 06/10/2017: Initial release
