#! /usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath('.'))

from multiwii import MultiWii

from serial import Serial
from time   import sleep

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

multiwii.arm()

sleep(2)

multiwii.disarm()
