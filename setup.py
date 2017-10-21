#!/usr/bin/python

"""Setup script for the unitconvert application"""

from setuptools import setup, find_packages

setup(
    name='unitconvert',
    version='1.0.1',
    license='MIT',
    author='Sky Maya',
    author_email='skymaya@gmail.com',
    url='https://github.com/skymaya/unitconvert',
    description="A command line tool for performing unit conversions",
    long_description=open("README.md", "r").read(),
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['unitconvert=unitconvert.runconvert:main'],
    },
    keywords="unitconvert conversions units",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        ],
)
