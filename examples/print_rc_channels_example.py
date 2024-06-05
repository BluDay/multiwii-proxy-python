#! /usr/bin/env python3

from multiwii import MultiWii

from multiwii.commands import MSP_RC

from serial import Serial

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

rc = multiwii.get_data(MSP_RC)

print(rc.roll)
print(rc.pitch)
print(rc.yaw)
print(rc.throttle)
print(rc.aux1)
print(rc.aux2)
print(rc.aux3)
print(rc.aux4)
