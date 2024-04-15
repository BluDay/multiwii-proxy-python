from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

class MultiWiiDataStructure(ABC):
    """Represents the base class for MSP data structure classes."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int]

    STRUCT_FORMAT: Final[str]

    # ----------------------------------- INSTANCE METHODS -------------------------------------
    
    @abstractmethod
    def _update(self, data: bytes) -> NoReturn:
        """Deserialize bytes to a derived data structure type."""
        pass

def msp_command_code(code: int) -> Callable[[int], Type]:
    """Decorator for setting the command code of a data structure."""
    def set_code(cls: Type) -> Type:
        """Sets the command code."""
        cls.COMMAND_CODE = code

        return cls

    return set_code

def msp_data_struct_format(format: str) -> Callable[[str], Type]:
    """Decorator for setting the struct format for data values."""
    def set_format(cls: Type) -> Type:
        """Sets the data format."""
        cls.STRUCT_FORMAT = format

        return cls

    return set_format
