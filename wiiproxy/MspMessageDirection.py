from typing import Final

class MspMessageDirection(object):
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
    The error character as a byte.
    """
    ERROR_BYTE: Final[int] = _serialize_to_int8(ERROR)

    """
    The incoming direction character as a byte.
    """
    INCOMING_BYTE: Final[int] = _serialize_to_int8(INCOMING)

    """
    The outgoing direction character as a byte.
    """
    OUTGOING_BYTE: Final[int] = _serialize_to_int8(OUTGOING)

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
