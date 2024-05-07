from typing import Final

class MspMessageDirection(object):
    """An enum-like class for message direction characters."""

    """The error character."""
    ERROR_CHAR: Final[str] = '!'
    
    """The incoming direction character."""
    INCOMING_CHAR: Final[str] = '<'

    """The outgoing direction character."""
    OUTGOING_CHAR: Final[str] = '>'
    
    """A serialized error character."""
    SERIALIZED_ERROR_CHAR: Final[int] = None

    """A serialized incoming direction character."""
    SERIALIZED_INCOMING_CHAR: Final[int] = None

    """A serialized outgoing direction character."""
    SERIALIZED_OUTGOING_CHAR: Final[int] = None
