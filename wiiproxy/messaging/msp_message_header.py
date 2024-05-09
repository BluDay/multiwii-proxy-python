from . import MspMessageDirection

from typing import Final

class MspMessageHeader(object):
    """An enum-like class for pre-built MSP message headers."""

    PREAMBLE: Final[str] = '$M'

    INCOMING: Final[str] = PREAMBLE + MspMessageDirection.INCOMING_CHAR

    OUTGOING: Final[str] = PREAMBLE + MspMessageDirection.OUTGOING_CHAR

    SERIALIZED_PREAMBLE: Final[bytes] = None

    SERIALIZED_INCOMING: Final[bytes] = None

    SERIALIZED_OUTGOING: Final[bytes] = None
