class _MultiWiiMessageHandler(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """
    The fixed MultiWii preamble used for all messages.
    """
    __MESSAGE_PREAMBLE: str = '$M'

    """
    The incoming direction character for an incoming MultiWii message.
    """
    __MESSAGE_DIRECTION_INCOMING: str = '<'

    """
    The outgoing direction character for an incoming MultiWii message.
    """
    __MESSAGE_DIRECTION_OUTGOING: str = '>'

    """
    The preamble as bytes.
    """
    __MESSAGE_PREAMBLE_BYTES: bytes = __MESSAGE_PREAMBLE.encode('ascii')

    """
    The incoming direction character as a byte.
    """
    __MESSAGE_DIRECTION_INCOMING_BYTE: int = __MESSAGE_DIRECTION_INCOMING & 0xff

    """
    The outgoing direction character as a byte.
    """
    __MESSAGE_DIRECTION_OUTGOING_BYTE: int = __MESSAGE_DIRECTION_OUTGOING & 0xff


    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_crc(data: bytes) -> int:
        """
        Calculates the a single byte checksum using CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): A serialized payload buffer.

        Returns:
            int: The calculated CRC value for the provided payload.
        """
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum

    # ------------------------------------- CLASS METHODS --------------------------------------

    @classmethod
    def get_incoming_direction_character(cls) -> str:
        """
        Gets the incoming message direction character.

        Returns:
            str: The direction character as a string.
        """
        return cls.__MESSAGE_DIRECTION_INCOMING

    @classmethod
    def get_outgoing_direction_character(cls) -> str:
        """
        Gets the outgoing message direction character.

        Returns:
            str: The direction character as a string.
        """
        return cls.__MESSAGE_DIRECTION_OUTGOING

    @classmethod
    def get_preamble(cls) -> str:
        """
        Gets the fixed MultiWii preamble string.

        Returns:
            str: Really?
        """
        return cls.__MESSAGE_PREAMBLE
