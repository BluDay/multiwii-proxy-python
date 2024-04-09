from . import MultiWiiMessageDirection

from typing import Final

class MultiWiiMessageHeader(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

    """
    The fixed MSP v1 preamble used for all messages.
    """
    PREAMBLE: Final[str] = '$M'

    """
    The incoming header.
    """
    INCOMING: Final[str] = _get_incoming_header()

    """
    The outgoing header.
    """
    OUTGOING: Final[str] = _get_outgoing_header()

    """
    A serialized preamble.
    """
    SERIALIZED_PREAMBLE: Final[bytes] = _encode(PREAMBLE)

    """
    A serialized incoming header.
    """
    SERIALIZED_INCOMING: Final[bytes] = _encode(INCOMING)

    """
    A serialized outgoing header.
    """
    SERIALIZED_OUTGOING: Final[bytes] = _encode(OUTGOING)

    # ------------------------------------- CLASS METHODS --------------------------------------

    @classmethod
    def _get_incoming_header(cls) -> str:
        """
        Gets the header for an incoming message.
        """
        return cls.PREAMBLE + MultiWiiMessageDirection.INCOMING

    @classmethod
    def _get_outgoing_header(cls) -> str:
        """
        Gets the header for an outgoing message.
        """
        return cls.PREAMBLE + MultiWiiMessageDirection.OUTGOING

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def _encode(value: str) -> bytes:
        """
        Converts a string to an ASCII-encoded byte array.

        Parameters:
            value (str): String to be encoded.

        Returns:
            bytes: ASCII-encoded string.
        """
        return value.encode('ascii')
