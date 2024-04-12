#! /usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wiiproxy.messaging.msp_commands       import MspCommands
from wiiproxy.messaging.msp_message_header import MspMessageHeader

print(MspMessageHeader.PREAMBLE)
print(MspMessageHeader.INCOMING)
print(MspMessageHeader.OUTGOING)

print(MspMessageHeader.SERIALIZED_PREAMBLE)
print(MspMessageHeader.SERIALIZED_INCOMING)
print(MspMessageHeader.SERIALIZED_OUTGOING)

print(MspCommands.IDENT)

"""
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

fc.start()

print(f'{fc.indent.multitype}') # QuadX
"""
