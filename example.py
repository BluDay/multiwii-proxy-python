#! /usr/bin/env python3

from wiiproxy.msp_commands import MSP_IDENT, MSP_MISC, MSP_RC
from wiiproxy.msp_config   import MultiWiiMultitype
from wiiproxy.msp_message  import MspMessage

print(f'Header preamble: {MspMessage.HEADER_PREAMBLE}')
print(f'Incoming header: {MspMessage.INCOMING_HEADER}')
print(f'Outgoing header: {MspMessage.OUTGOING_HEADER}')

print(repr(MSP_IDENT))
print(repr(MSP_MISC))
print(repr(MSP_RC))

print(MultiWiiMultitype.Ident)
