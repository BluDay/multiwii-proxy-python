#! /usr/bin/env python3

from multiwii import MultiWii
from serial   import Serial
from time     import sleep

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

multiwii.arm()

sleep(2)

multiwii.disarm()