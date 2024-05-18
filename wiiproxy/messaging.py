from typing import Final

class MspMessage(object):
    """A utility for handling MSP messages."""

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    HEADER_PREAMBLE: Final[bytes] = b'$M' # 0x24, 0x4d

    ERROR_CHAR: Final[bytes] = b'!' # 0x21
 
    INCOMING_CHAR: Final[bytes] = b'<' # 0x3c

    OUTGOING_CHAR: Final[bytes] = b'>' # 0x3e

    ERROR_HEADER: Final[bytes] = HEADER_PREAMBLE + ERROR_CHAR

    INCOMING_HEADER: Final[bytes] = HEADER_PREAMBLE + INCOMING_CHAR

    OUTGOING_HEADER: Final[bytes] = HEADER_PREAMBLE + OUTGOING_CHAR

    # ------------------------------------- STATIC METHODS -------------------------------------

    @classmethod
    def decode_names(cls, data: bytes) -> tuple[str]:
        """Decodes the deserialized string value and splits it to a tuple.

        Raises
        ------
        TypeError
            If `data` is not of type `bytes`.
        UnicodeDecodeError
            If the bytes cannot be decoded into ASCII characters.
        """
        return tuple(data.decode('ascii').split(';'))

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC."""
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum & 0xff
