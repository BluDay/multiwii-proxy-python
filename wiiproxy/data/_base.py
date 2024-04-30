from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

class _MultiWiiData(ABC):
    """Represents the base class for MSP data structure classes."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    """The corresponding MSP command code."""
    COMMAND_CODE: Final[int]

    """Whether the data size is indeterminate or not."""
    HAS_VARIABLE_SIZE: Final[bool]

    """The structure format in a string literal value."""
    STRUCT_FORMAT: Final[str]

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _raw_data: bytes

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance."""
        self._raw_data = None

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
