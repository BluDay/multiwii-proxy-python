from struct import calcsize
from typing import Final, NoReturn, Self

class MspCommand(object):
    """Represents a MSP command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _code: Final[int]

    _has_variable_size: Final[bool]

    _is_set_command: Final[bool]

    _struct_format: Final[str]

    _struct_format_size: Final[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, code: int, struct_format: str) -> NoReturn:
        """Initializes an instance using the provided code and struct format.

        Raises
        ------
        ValueError
            If the provided code is not between 100 or 240.
            If the a format has not been provided for a set command.
        """
        if not 100 <= code <= 250:
            raise ValueError('Command code must be between 100 and 240.')

        self._code = code

        self._is_set_command = code >= 200

        if struct_format:
            has_variable_size = struct_format[0] == '*'

            if has_variable_size:
                struct_format = struct_format[1:]

            self._has_variable_size = has_variable_size

            self._struct_format_size = calcsize(f'<{struct_format}')
            self._struct_format      = struct_format

            return

        self._has_variable_size = False

        self._struct_format      = None
        self._struct_format_size = None

    def __repr__(self) -> str:
        """Gets a string representation of the object."""
        return f'{self.__class__.__name__}<{self._code}, {self._struct_format}>'

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def code(self) -> int:
        """Gets the command code."""
        return self._code

    @property
    def has_variable_size(self) -> int:
        """Gets a value indicative whether the data structure size is indeterminate."""
        return self._has_variable_size

    @property
    def struct_format(self) -> str:
        """Gets the data structure format to use with the `struct` module."""
        return self._struct_format

    @property
    def struct_format_size(self) -> int:
        """Gets the data structure format size."""
        return self._struct_format_size
