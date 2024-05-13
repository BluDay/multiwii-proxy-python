#! /usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wiiproxy.msp_message import MspMessage
from wiiproxy.msp_data    import MspIdent, MspRawImu

print(f'Header preamble: {MspMessage.HEADER_PREAMBLE}')
print(f'Incoming header: {MspMessage.INCOMING_HEADER}')
print(f'Outgoing header: {MspMessage.OUTGOING_HEADER}')
