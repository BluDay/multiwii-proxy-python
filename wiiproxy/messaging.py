from typing import Final

class MspMessage(object):
    """A utility for handling MSP messages."""

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    ERROR_HEADER:    Final[bytes] = b'$M!' # 0x24, 0x4d, 0x21

    INCOMING_HEADER: Final[bytes] = b'$M<' # 0x24, 0x4d, 0x3c

    OUTGOING_HEADER: Final[bytes] = b'$M>' # 0x24, 0x4d, 0x3e

    # ------------------------------------- STATIC METHODS -------------------------------------

    @classmethod
    def decode_names(cls, data: tuple) -> tuple[str]:
        """Decodes the deserialized string value and splits it to a tuple.

        Raises
        ------
        TypeError
            If `data` is not of type `tuple`.
        UnicodeDecodeError
            If the bytes cannot be decoded into ASCII characters.
        """
        return tuple(data[0].decode('ascii').split(';'))

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC."""
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum & 0xff
