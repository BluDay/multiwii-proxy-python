#! /usr/bin/env python3

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

print(multiwii.get_data(MSP_ANALOG))
print(multiwii.get_data(MSP_IDENT))
print(multiwii.get_data(MSP_MISC))
print(multiwii.get_data(MSP_STATUS))