from wiiproxy.messaging.MultiWiiMessageDirection import MultiWiiMessageDirection

from typing import Final

class MultiWiiMessageHeader(object):
    """The class for managing and analyzing MultiWii messages."""

    """The fixed MSP v1 preamble used for all messages."""
    PREAMBLE: Final[str] = '$M'

    """The incoming header."""
    INCOMING: Final[str] = f'{PREAMBLE}{MultiWiiMessageDirection.INCOMING}'

    """The outgoing header."""
    OUTGOING: Final[str] = f'{PREAMBLE}{MultiWiiMessageDirection.OUTGOING}'

    """ A serialized preamble."""
    SERIALIZED_PREAMBLE: Final[bytes] = int() # encode(PREAMBLE)

    """A serialized incoming header."""
    SERIALIZED_INCOMING: Final[bytes] = int() # encode(INCOMING)

    """A serialized outgoing header."""
    SERIALIZED_OUTGOING: Final[bytes] = int() # encode(OUTGOING)
