class _MultiWiiMessageHandler(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    _MESSAGE_PREAMBLE: str = '$M'

    _MESSAGE_DIRECTION_INCOMING: str = '<'

    _MESSAGE_DIRECTION_OUTGOING: str = '>'

    @classmethod
    def get_message_direction_char(cls, incoming: bool = True) -> str:
        """
        Gets the incoming or outgoing message direction character depending on the
        provided boolean value.

        Parameters:
            incoming (bool): Determines the direction character.

        Returns:
            str: The direction character as a string.
        """
        if incoming:
            return cls._MESSAGE_DIRECTION_INCOMING

        return cls._MESSAGE_DIRECTION_OUTGOING

    @classmethod
    def get_message_preamble(cls) -> str:
        """
        Gets the fixed MultiWii preamble string.

        Returns:
            str: Really?
        """
        return cls._MESSAGE_PREAMBLE
