from .       import WiiProxy
from .config import PriorityType

from struct import calcsize

class MultiWiiCommand(object):
    """Represents a descriptor for a MultiWii command.

    This class contains information about a command, such as the code and format of the command.
    """

    def __init__(
        self,
        code:          int,
        format:        str,
        is_dynamic:    bool,
        priority_type: PriorityType
    ) -> None:
        """Initializes an instance with all necessary parameters."""
        self._code = code

        self._format = format

        self._is_dynamic = is_dynamic

        self._priority_type = priority_type

        self._size = calcsize(WiiProxy._ENDIANNNESS + format)
    
    @property
    def code(self) -> int:
        """int: Gets the code of the command."""
        return self._code

    @property
    def format(self) -> str:
        """str: Gets the `struct` format for the data values."""
        return self._format

    @property
    def is_dynamic(self) -> bool:
        """bool: Gets a value indicative whether the data size is indeterminate."""
        return self._is_dynamic

    @property
    def priority_type(self) -> PriorityType:
        """PriorityType: Gets the priority of the command."""
        return self._priority_type
    
    @property
    def size(self) -> int:
        """int: Gets the total byte size of the data values."""
        return self._size
