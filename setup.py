#! /usr/bin/env python3

from setuptools import setup

from wiiproxy import (
    __author__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__
)

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author=__author__,
    license=__license__,
    packages=['wiiproxy'],
    requires=(
        'pyserial==3.4,3.5',
        'pytest>=8.1.1'
    )
)
