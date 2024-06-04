#! /usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath('.'))

from wiiproxy.commands import MSP_IDENT, MSP_MISC, MSP_RC

from wiiproxy.config import MultiWiiMultitype

from wiiproxy.data import MspRc

from wiiproxy.messaging import (
    MESSAGE_ERROR_HEADER,
    MESSAGE_INCOMING_HEADER,
    MESSAGE_OUTGOING_HEADER
)

print(f'Error header    : {MESSAGE_ERROR_HEADER}')
print(f'Incoming header : {MESSAGE_INCOMING_HEADER}')
print(f'Outgoing header : {MESSAGE_OUTGOING_HEADER}')

print(repr(MSP_IDENT))
print(repr(MSP_MISC))
print(repr(MSP_RC))

print(repr(MultiWiiMultitype.QuadX))
