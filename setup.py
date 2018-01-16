#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Tardis-Selenium',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0',

    description='Tardis Selenium',
    url='ssh://git@bitbucket.agile.bns:7999/tardis/tardis_selenium.git',
    classifiers=['python3']
)

