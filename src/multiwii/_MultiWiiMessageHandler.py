from typing import Final

class _MultiWiiMessageHandler(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

     """
    The error character.
    """
    MESSAGE_ERROR_CHAR: Final[str] = '!'

    """
    The incoming direction character.
    """
    MESSAGE_INCOMING_CHAR: Final[str] = '<'

    """
    The outgoing direction character.
    """
    MESSAGE_OUTGOING_CHAR: Final[str] = '>'

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
    The error character as a byte.
    """
    MESSAGE_SERIALIZED_ERROR_CHAR: Final[int] = __int8(MESSAGE_ERROR_CHAR)

    """
    The incoming character as a byte.
    """
    MESSAGE_SERIALIZED_INCOMING_CHAR: Final[int] = __int8(MESSAGE_INCOMING_CHAR)

    """
    The outgoing character as a byte.
    """
    MESSAGE_SERIALIZED_OUTGOING_CHAR: Final[int] = __int8(MESSAGE_OUTGOING_CHAR)

    """
    The preamble in bytes.
    """
    MESSAGE_SERIALIZED_PREAMBLE: Final[bytes] = __encode(MESSAGE_PREAMBLE)

    """
    The serialized incoming header.
    """
    MESSAGE_SERIALIZED_INCOMING_HEADER: Final[bytes] = __encode(MESSAGE_INCOMING_HEADER)

    """
    The serialized outgoing header.
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
            direction = cls.MESSAGE_INCOMING_CHAR
        else
            direction = cls.MESSAGE_OUTGOING_CHAR

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
    def __int8(value: str) -> int:
        """
        Serializes the provided string value to a signed 8-bit integer.

        Parameters:
            value (str): The string value to be serialized.

        Returns:
            int: The serialized 8-bit integer.
        """
        return ord(value) & 0xff

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
