#! /usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wiiproxy      import MspMessage
from wiiproxy.data import MspIdent, MspRawImu

print(f'Header preamble: {MspMessage.HEADER_PREAMBLE}')
print(f'Incoming header: {MspMessage.INCOMING_HEADER}')
print(f'Outgoing header: {MspMessage.OUTGOING_HEADER}')

print(f'MSP_IDENT ({MspIdent.COMMAND_CODE})')
print(f'MSP_RAW_IMU ({MspRawImu.COMMAND_CODE})')

"""
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

fc.start()

print(f'{fc.indent.multitype}') # QuadX
"""
