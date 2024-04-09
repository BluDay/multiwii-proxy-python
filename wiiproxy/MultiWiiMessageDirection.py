from typing import Final

class MultiWiiMessageDirection(object):
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
    
    """
    A serialized error character.
    """
    SERIALIZED_ERROR: Final[int] = _serialize_to_int8(ERROR)

    """
    A serialized incoming direction character.
    """
    SERIALIZED_INCOMING: Final[int] = _serialize_to_int8(INCOMING)

    """
    A serialized outgoing direction character.
    """
    SERIALIZED_OUTGOING: Final[int] = _serialize_to_int8(OUTGOING)

    # ------------------------------------- CLASS METHODS --------------------------------------

    def _serialize_to_int8(value: str) -> int:
        """
        Gets the value of the first character as an 8-bit signed integer.

        Parameters:
            value (str): The value to serialize.

        Returns:
            int: The serialized value.
        """
        return ord(value) & 0xff
