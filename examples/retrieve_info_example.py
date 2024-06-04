#! /usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath('.'))

from multiwii import MultiWii

from multiwii.commands import (
    MSP_ANALOG,
    MSP_IDENT,
    MSP_MISC,
    MSP_STATUS
)

from serial import Serial

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

analog = multiwii.get_data(MSP_ANALOG)
ident  = multiwii.get_data(MSP_IDENT)
misc   = multiwii.get_data(MSP_MISC)
status = multiwii.get_data(MSP_STATUS)

print(analog)
print(ident)
print(misc)
print(status)
