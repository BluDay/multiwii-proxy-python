#! /usr/bin/env python3

from setuptools import setup

setup(
    name='multiwii-proxy-python',
    version='3.0',
    description='A simple and user-friendly Python 3 module for MultiWii-based drones.',
    url='https://bluday.github.io/multiwii-proxy-python',
    author='BluDay',
    license='MIT',
    packages=('multiwii'),
    requires=('pyserial==3.4,3.5')
)
