#! /usr/bin/env python3

from setuptools import setup

setup(
    name='WiiProxy',
    version='1.0',
    description='A simple and user-friendly Python 3 module for MultiWii-based drones.',
    url='https://github.com/BluDay/wiiproxy',
    author='BluDay',
    license='MIT',
    packages=(
        'wiiproxy'
    ),
    requires=(
        'pyserial==3.4,3.5',
        'pytest>=8.1.1'
    )
)
