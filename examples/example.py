#! /usr/bin/env python3

from wiiproxy.messaging.MultiWiiMessageHeader import MultiWiiMessageHeader

from wiiproxy.messaging.MultiWiiCommands import MultiWiiCommands

print(MultiWiiMessageHeader.PREAMBLE)
print(MultiWiiMessageHeader.INCOMING)
print(MultiWiiMessageHeader.OUTGOING)

print(MultiWiiMessageHeader.SERIALIZED_PREAMBLE)
print(MultiWiiMessageHeader.SERIALIZED_INCOMING)
print(MultiWiiMessageHeader.SERIALIZED_OUTGOING)

print(MultiWiiCommands.MSP_IDENT)

"""
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

print(f'{fc.indent.multitype}') # QuadX
"""
