class MspMessageData(object):
    """A utility for managing MSP message data."""

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_checksum(data: bytes) -> int:
        """Calculates the checksum for the data values using an XOR CRC."""
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum & 0xff
