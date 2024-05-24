from struct import calcsize
from typing import Final, NoReturn

class Command(object):
    """Represents an MSP command.

    This class encapsulates the details of a command for the MultiWii Serial Protocol (MSP).
    It includes information about the command code, whether the command size is variable,
    if it is a set-command, and details about the structure format used for serializing and
    deserializing corresponding data values.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _code: Final[int]

    _data_field_count: Final[int]

    _data_size: Final[int]

    _has_variable_size: Final[bool]

    _is_set_command: Final[bool]

    _payload_struct_format: Final[str]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, code: int, data_format: str = None) -> NoReturn:
        """Initializes an instance using the provided code and struct format.

        Note
        ----
        This constructor will use `struct.calcsize` to calculate the data size of the data
        structure format, and to validate the format string itself. Invalid format strings
        will cause `struct.calcsize` to raise an exception of type `struct.error`.

        Parameters
        ----------
        code : int
            The unique code representing the specific MSP command. Must be between 100 and 240.
        data_format : str
            The `struct` format string used for packing and unpacking a corresponding payload.

        Raises
        ------
        ValueError
            If the provided code is not between 100 or 250.
        """
        if not 100 <= code <= 250:
            raise ValueError('Command code must be between 100 and 250.')

        data_struct_format = None
        data_field_count   = 0
        has_variable_size  = False

        if data_format:
            format_properties = data_format.split(':')

            data_struct_format = format_properties[0]
            data_field_count   = int(format_properties[1])
            has_variable_size  = format_properties[2] == '?'

        self._code = code

        self._has_variable_size = has_variable_size

        self._is_set_command = code >= 200

        if not data_struct_format:
            self._data_field_count = 0
            self._data_size        = 0

            self._payload_struct_format = None 

            return

        self._data_size        = calcsize(f'<{data_struct_format}') 
        self._data_field_count = data_field_count

        self._payload_struct_format = f'<2B{data_struct_format}'

    def __int__(self) -> int:
        """Returns the integer representation of the object, as the MSP command code.

        Returns
        -------
        int
            The MSP command code.
        """
        self._code

    def __repr__(self) -> str:
        """Returns a string representation of the object.

        This method perform formats a string using the following values:

            * Class name
            * Command code
            * Data structure format
            * Data size

        Returns
        -------
        str
            A detailed string representation of the object.
        """
        data_struct_format = self.data_struct_format

        if self._has_variable_size:
            data_struct_format = f'*{data_struct_format}'

        return '{}<{}, "{}", {}, {}, "{}">'.format(
            self.__class__.__name__,
            self._code,
            data_struct_format,
            self._data_size,
            self._data_field_count,
            '?' if self._has_variable_size else '!'
        )

    def __str__(self) -> str:
        """Returns the string representation of the object, as the data structure format.

        Returns
        -------
        str
            The data structure format string.
        """
        return self.data_struct_format

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def code(self) -> int:
        """Gets the unique command code.

        Returns
        -------
        int
            The unique MSP command code.
        """
        return self._code

    @property
    def data_field_count(self) -> int:
        """Gets the data field count.

        Returns
        -------
        int
            The field count for the provided data structure format.
        """
        return self._data_field_count

    @property
    def data_size(self) -> int:
        """Gets the data structure size.

        Returns
        -------
        int
            The data structure size.
        """
        return self._data_size

    @property
    def data_struct_format(self) -> str:
        """Gets the data structure format string.

        Returns
        -------
        str
            The data structure format that was provided initially.
        """
        format = self._payload_struct_format

        return format[3:] if format else None

    @property
    def has_variable_size(self) -> bool:
        """Gets a value indicative whether the data size is variable.

        Returns
        -------
        bool
            True if data size is variable, False otherwise.
        """
        return self._has_variable_size

    @property
    def is_set_command(self) -> bool:
        """Gets a value indicative whether the command is a set-command.
        
        Returns
        -------
        bool
            True if the command is a set-command, False otherwise.
        """
        return self._is_set_command

    @property
    def payload_struct_format(self) -> str:
        """Gets the payload format string.

        Returns
        -------
        str
            The payload struct format string.
        """
        return self._payload_struct_format
