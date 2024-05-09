from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

class _MspDataStructure(ABC):
    """Represents the base class for MSP data structure classes."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int]

    HAS_VARIABLE_SIZE: Final[bool]

    STRUCT_FORMAT: Final[str]

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    @abstractmethod
    def update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        pass

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
