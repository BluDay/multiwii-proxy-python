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
    MESSAGE_INCOMING_HEADER: Final[str] = __get_header()

    """
    The outgoing header.
    """
    MESSAGE_OUTGOING_HEADER: Final[str] = __get_header(incoming=False)

    """
    The preamble in encoded bytes.
    """
    MESSAGE_SERIALIZED_PREAMBLE: Final[bytes] = __encode(MESSAGE_PREAMBLE)

    """
    The incoming header in encoded bytes.
    """
    MESSAGE_SERIALIZED_INCOMING_HEADER: Final[bytes] = __encode(MESSAGE_INCOMING_HEADER)
    
    """
    The outgoing header in encoded bytes.
    """
    MESSAGE_SERIALIZED_OUTGOING_HEADER: Final[bytes] = __encode(MESSAGE_OUTGOING_HEADER)

    # ------------------------------------- CLASS METHODS --------------------------------------

    @classmethod
    def __get_header(cls, incoming: bool = True) -> str:
        """
        Gets a header for a specific direction.

        Parameters:
            incoming (bool): Whether the direction character should be incoming or outgoing.

        Returns:
            str: The full header string value.
        """
        direction: str

        if incoming:
            direction = MspMessageDirection.INCOMING
        else:
            direction = MspMessageDirection.OUTGOING

        return cls.MESSAGE_PREAMBLE + direction

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def __encode(value: str) -> bytes:
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
