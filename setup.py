#! /usr/bin/env python3

from setuptools import setup

from wiiproxy import (
    __author__,
    __license__,
    __version
)

setup(
    name='wiiproxy',
    version=__version__,
    description='User-friendly Python 3 module for MultiWii-based drones',
    url='https://github.com/BluDay/wiiproxy',
    author=__author__,
    license=__license__,
    packages=('wiiproxy',)
)
