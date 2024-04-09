from . import MspMessageDirection

from typing import Final

class MspMessage(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

    """
    The fixed MSP v1 preamble used for all messages.
    """
    MESSAGE_PREAMBLE: Final[str] = '$M'

    """
    The incoming header.
    """
    MESSAGE_INCOMING_HEADER: Final[str] = _get_incoming_header()

    """
    The outgoing header.
    """
    MESSAGE_OUTGOING_HEADER: Final[str] = _get_outgoing_header()

    """
    The preamble in encoded bytes.
    """
    MESSAGE_PREAMBLE_BYTES: Final[bytes] = _encode(MESSAGE_PREAMBLE)

    """
    The incoming header in encoded bytes.
    """
    MESSAGE_INCOMING_HEADER_BYTES: Final[bytes] = _encode(MESSAGE_INCOMING_HEADER)

    """
    The outgoing header in encoded bytes.
    """
    MESSAGE_OUTGOING_HEADER_BYTES: Final[bytes] = _encode(MESSAGE_OUTGOING_HEADER)

    # ------------------------------------- CLASS METHODS --------------------------------------

    @classmethod
    def _get_incoming_header(cls) -> str:
        """
        Gets the header for an incoming message.
        """
        return cls.MESSAGE_PREAMBLE + MspMessageDirection.INCOMING

    @classmethod
    def _get_outgoing_header(cls) -> str:
        """
        Gets the header for an outgoing message.
        """
        return cls.MESSAGE_PREAMBLE + MspMessageDirection.OUTGOING

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def _encode(value: str) -> bytes:
        """
        Converts a string to an ASCII-encoded byte array.

        Parameters:
            value (str): String to be encoded.

        Returns:
            bytes: ASCII-encoded string.
        """
        return value.encode('ascii')

    @staticmethod
    def calculate_crc(payload: bytes) -> int:
        """
        Calculates the checksum for the payload using an XOR CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): The serialized payload.

        Returns:
            int: The calculated checksum value.
        """
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum
