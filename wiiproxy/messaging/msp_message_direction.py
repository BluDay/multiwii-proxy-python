from struct import pack
from typing import Final

class MspMessageDirection(object):
    """An enum-like class for MSP message direction characters."""

    ERROR_CHAR: Final[str] = '!'
    
    INCOMING_CHAR: Final[str] = '<'

    OUTGOING_CHAR: Final[str] = '>'
    
    SERIALIZED_ERROR_CHAR: Final[int] = None

    SERIALIZED_INCOMING_CHAR: Final[int] = None

    SERIALIZED_OUTGOING_CHAR: Final[int] = None
