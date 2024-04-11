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
