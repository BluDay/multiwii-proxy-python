from typing import Final

class MspMessage(object):
    """A utility for handling MSP messages."""

    HEADER_PREAMBLE: Final[bytes] = b'$M' # 0x24, 0x4d

    ERROR_CHAR: Final[int] = 0x21 # !
 
    INCOMING_CHAR: Final[int] = 0x3c # <

    OUTGOING_CHAR: Final[int] = 0x3e # >

    ERROR_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(ERROR_CHAR).encode('ascii')

    INCOMING_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(INCOMING_CHAR).encode('ascii')

    OUTGOING_HEADER: Final[bytes] = HEADER_PREAMBLE + chr(OUTGOING_CHAR).encode('ascii')

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_checksum(data: bytes) -> int:
        """Calculates the checksum for the data values using an XOR CRC."""
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum & 0xff
