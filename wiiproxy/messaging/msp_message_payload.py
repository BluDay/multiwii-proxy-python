class MspMessagePayload(object):
    """A utility with various payload-related methods."""

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC."""
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum & 0xff
