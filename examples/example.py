#! /usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wiiproxy.data import Ident, RawImu

from wiiproxy.messaging import MspMessageHeader

print(f'Header preamble: "{MspMessageHeader.PREAMBLE}" ({MspMessageHeader.SERIALIZED_PREAMBLE})')
print(f'Incoming header: "{MspMessageHeader.INCOMING}" ({MspMessageHeader.SERIALIZED_INCOMING})')
print(f'Outgoing header: "{MspMessageHeader.OUTGOING}" ({MspMessageHeader.SERIALIZED_OUTGOING})')

print(f'MSP_IDENT ({Ident.COMMAND_CODE})')
print(f'MSP_RAW_IMU ({RawImu.COMMAND_CODE})')

"""
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

fc.start()

print(f'{fc.indent.multitype}') # QuadX
"""
