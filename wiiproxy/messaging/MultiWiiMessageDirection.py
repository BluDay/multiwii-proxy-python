from typing import Final

class MultiWiiMessageDirection(object):
    """An enum-like class for message direction characters.

    Includes additional methods for retrieving each direction character as a serialized value.
    """

    """The error character."""
    ERROR: Final[str] = '!'
    
    """The incoming direction character."""
    INCOMING: Final[str] = '<'

    """The outgoing direction character."""
    OUTGOING: Final[str] = '>'
    
    """A serialized error character."""
    SERIALIZED_ERROR: Final[int] = 0 # serialize_to_int8(ERROR)

    """A serialized incoming direction character."""
    SERIALIZED_INCOMING: Final[int] = 0 # serialize_to_int8(INCOMING)

    """A serialized outgoing direction character."""
    SERIALIZED_OUTGOING: Final[int] = 0 # serialize_to_int8(OUTGOING)
