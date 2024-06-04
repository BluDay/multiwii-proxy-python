#! /usr/bin/env python3

from setuptools import setup

setup(
    name='WiiProxy',
    version='3.0',
    description='A simple and user-friendly Python 3 module for MultiWii-based drones.',
    url='https://bluday.github.io/wiiproxy',
    author='BluDay',
    license='MIT',
    packages=('wiiproxy'),
    requires=('pyserial==3.4,3.5')
)
