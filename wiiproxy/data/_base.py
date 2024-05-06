from ..config import CommandPriority

from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

class _MspDataStructure(ABC):
    """Represents the base class for MSP data structure classes."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int]

    HAS_VARIABLE_SIZE: Final[bool]

    STRUCT_FORMAT: Final[str]

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _priority: CommandPriority

    _raw_data: bytes

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance."""
        self._raw_data = None

        self._priority = CommandPriority.Normal

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def priority(self) -> CommandPriority:
        """Gets the current priority for the corresponding command."""
        return self._priority

    @priority.setter
    def priority(self, value: CommandPriority) -> NoReturn:
        """Sets the priority to be used for the corresponding command."""
        if not isinstance(value, CommandPriority):
            raise TypeError('Value must be of type "CommandPriority".')

        self._priority = value

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    @abstractmethod
    def _evaluate_raw_data(self) -> NoReturn:
        """Evaluates received raw data values and updates derived instance members."""
        pass
    
    def update(self, raw_data: bytes) -> NoReturn:
        """Deserialize bytes to a derived data structure type.

        Parameters:
            data (bytes): A buffer with the raw data values.
        """
        self._raw_data = data

        self._evaluate_raw_data()

def command_code(code: int) -> Callable[[int], Type]:
    """Decorator for setting the command code of a data structure."""
    def set_code(cls: Type) -> Type:
        """Sets the command code."""
        cls.COMMAND_CODE = code

        return cls

    return set_code

def struct_format(format: str, has_variable_size: bool = False) -> Callable[[str], Type]:
    """Decorator for setting the struct format for data values."""
    def set_format(cls: Type) -> Type:
        """Sets format-related class member values in the given structure type."""
        cls.HAS_VARIABLE_SIZE = has_variable_size

        cls.STRUCT_FORMAT = format

        return cls

    return set_format
