from typing import Final

class MspMessage(object):
    """A utility for handling MSP messages."""

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    _ENCODING: Final[str] = 'ascii'

    _NAME_SEPARATION_CHAR: Final[str] = ';'

    HEADER_PREAMBLE: Final[bytes] = b'$M' # 0x24, 0x4d

    ERROR_CHAR: Final[int] = 0x21 # !
 
    INCOMING_CHAR: Final[int] = 0x3c # <

    OUTGOING_CHAR: Final[int] = 0x3e # >

    ERROR_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(ERROR_CHAR).encode(_ENCODING)

    INCOMING_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(INCOMING_CHAR).encode(_ENCODING)

    OUTGOING_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(OUTGOING_CHAR).encode(_ENCODING)

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
        return tuple(data.decode(cls._ENCODING).split(cls._NAME_SEPARATION_CHAR))

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC."""
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum & 0xff
