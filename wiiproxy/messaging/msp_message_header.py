from . import MspMessageDirection

from typing import Final

class MspMessageHeader(object):
    """The class for managing and analyzing MultiWii messages."""

    """The fixed MSP v1 preamble used for all messages."""
    PREAMBLE: Final[str] = '$M'

    """The incoming header."""
    INCOMING: Final[str] = PREAMBLE + MspMessageDirection.INCOMING_CHAR

    """The outgoing header."""
    OUTGOING: Final[str] = PREAMBLE + MspMessageDirection.OUTGOING_CHAR

    """A serialized preamble."""
    SERIALIZED_PREAMBLE: Final[bytes] = None

    """A serialized incoming header."""
    SERIALIZED_INCOMING: Final[bytes] = None

    """A serialized outgoing header."""
    SERIALIZED_OUTGOING: Final[bytes] = None
