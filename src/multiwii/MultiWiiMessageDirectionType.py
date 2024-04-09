from typing import Final

class MultiWiiMessageDirectionType(object):
    """
    An enum-like class for message direction characters. Includes additional methods
    for retrieving each direction character as a serialized value.
    """

    """
    The error character.
    """
    ERROR: Final[str] = '!'

    """
    The incoming direction character.
    """
    INCOMING: Final[str] = '<'

    """
    The outgoing direction character.
    """
    OUTGOING: Final[str] = '>'

    # ------------------------------------- CLASS METHODS --------------------------------------

    def get_error_as_byte(cls) -> str:
        """
        Gets the error character as a byte.

        Returns:
            str: A serialized error character string.
        """
        return ord(cls.ERROR) & 0xff

    def get_incoming_as_byte(cls) -> str:
        """
        Gets the incoming character as a byte.

        Returns:
            str: A serialized error character string.

        """
        return ord(cls.INCOMING) & 0xff

    def get_outgoing_as_byte(cls) -> str:
        """
        Gets the outgoing character as a byte.

        Returns:
            str: A serialized error character string.

        """
        return ord(cls.OUTGOING) & 0xff
