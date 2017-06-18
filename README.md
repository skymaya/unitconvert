# Unitconvert: Unit conversion tool - Version 1.0.1

## Synopsis

A simple tool for converting amounts between various units of measurement.

## Testing

There is a "tests" directory containing some unit tests for some of the classes and functions in this application.

Additionally, the application has been tested on the following systems and python versions:

* Ubuntu 16.04 (python 3.5.2, python 2.7.12)

## Known Issues

* Fully untested on Windows, Mac, and BSD at this time

## Installation

Git clone this repo or download the source and unpack into a directory. Install with:

`sudo pip install /full/path/to/sourcedirectory`

Note: you may or may not need "sudo" but it was required for installing in my environment.

## Usage

After installation is completed, you may run the unitconvert tool using the following command:

`runconvert.py -h -a AMOUNT -f UNIT_FROM -t UNIT_TO`

Arguments:
* -a AMOUNT: Amount to convert
* -f UNIT_FROM: Unit to convert from
* -t UNIT_TO: Unit to convert to

Available unit types and unit arguments (in parentheses):

* Digital:
  - Decimal: Byte (B), Kilobyte (kB), Megabyte (MB), Gigabyte (GB), Terabyte (TB), Petabyte (PB), Exabyte (EB), Zettabyte (ZB), Yottabyte (YB)
  - Binary: Kibibyte (KiB), Mebibyte (MiB), Gibibyte (GiB), Tebibyte (TiB), Pebibyte (PiB), Exbibyte (EiB), Zebibyte (ZiB), Yobibyte (YiB)
* Length: Millimeter (mm), Centimeter (cm), Inch (in), Foot (ft), Yard (yd), Meter (m), Kilometer (km), Mile (mi)
* Time: Millisecond (ms), second (sec), Minute (min), Hour (hr), Day (day), Week (wk), Month (mo), Year (yr)
* Volume:
  - Metric: Milliliter (ml), Liter (l)
  - US customary: Teaspoon (tsp), Tablespoon (tbsp), fluid Ounces (floz), Cup (cup), Pint (pt), Quart (qt), Gallon (gal)
  - US legal: Cup (lcup)
  - Cubic: Cubic Inch (in3), Cubic Foot (ft3)
* Mass: Milligram (mg), Gram (g), Ounce (oz), Pound (lb), Kilogram (kg)
* Temperature: Fahrenheit (F), Celsius (C), Kelvin (K)

## Updating

If you want to update the application currently installed, just run the following after downloading the newest source files:

`sudo pip install /full/path/to/sourcedirectory --upgrade`

Note: you may or may not need "sudo" but it was required for updating in my environment.

## Uninstalling

If you want to uninstall the application, run the following:

`sudo pip uninstall sitemap`

Note: you may or may not need "sudo" but it was required for updating in my environment.

## To Do

* Add support for more units

## Contributors

Get in touch with me if you'd like to contribute.

## License

The code contained within this repository is released under the MIT license.

## Changelog

### Version 1.0.1
* 06/17/2017: Added fluid ounces

### Version 1.0.0
* 06/10/2017: Initial release
