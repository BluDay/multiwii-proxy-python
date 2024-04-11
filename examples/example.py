#! /usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wiiproxy.messaging import MultiWiiCommands, MultiWiiMessageHeader

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

fc.start()

print(f'{fc.indent.multitype}') # QuadX
"""
