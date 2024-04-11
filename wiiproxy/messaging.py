from typing import Final

class MultiWiiMessageDirection(object):
    """An enum-like class for message direction characters."""

    """The error character."""
    ERROR: Final[str] = '!'
    
    """The incoming direction character."""
    INCOMING: Final[str] = '<'

    """The outgoing direction character."""
    OUTGOING: Final[str] = '>'
    
    """A serialized error character."""
    SERIALIZED_ERROR: Final[int] = int() # serialize_to_int8(ERROR)

    """A serialized incoming direction character."""
    SERIALIZED_INCOMING: Final[int] = int() # serialize_to_int8(INCOMING)

    """A serialized outgoing direction character."""
    SERIALIZED_OUTGOING: Final[int] = int() # serialize_to_int8(OUTGOING)

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

class MultiWiiMessagePayload(object):
    """A utility with various payload-related methods."""

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): The serialized message payload.

        Returns:
            int: The checksum value.
        """
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum & 0xff
