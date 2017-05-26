#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='unitconvert',
    version='1.0',
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
        'Development Status :: 1.0 - Beta',
        'Environment :: Console',
        'Intended Audience :: General Audience',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Unit Conversions',
        ],
)
