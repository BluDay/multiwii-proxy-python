from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

class MultiWiiDataStructure(ABC):
    """Represents the base class for MSP data structure classes."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int]

    HAS_VARIABLE_SIZE: Final[bool]

    STRUCT_FORMAT: Final[str]

    # ----------------------------------- INSTANCE METHODS -------------------------------------
    
    @abstractmethod
    def _update(self, data: bytes) -> NoReturn:
        """Deserialize bytes to a derived data structure type."""
        pass

def command_code(code: int) -> Callable[[int], Type]:
    """Decorator for setting the command code of a data structure.

    Parameters:
        code (int): The command code as an integer.

    Returns:
        callable: The wrapped target method.
    """
    def set_code(cls: Type) -> Type:
        """Sets the command code.

        Parameters:
            cls (Type): The derived structure class type.

        Returns:
            type: The structure type.
        """
        cls.COMMAND_CODE = code

        return cls

    return set_code

def struct_format(format: str, has_variable_size: bool = False) -> Callable[[str], Type]:
    """Decorator for setting the struct format for data values.

    Parameters:
        format (str):
            The struct format to use for deserializing raw data buffers.
        
        has_variable_size (bool):
            Whether the structure has an indeterminate size.

    Returns:
        callable: The wrapped target method.
    """
    def set_format(cls: Type) -> Type:
        """Sets format-related class member values in the given structure type.

        Parameters:
            cls (Type): The derived structure class type.

        Returns:
            type: The structure type.
        """
        cls.HAS_VARIABLE_SIZE = has_variable_size

        cls.STRUCT_FORMAT = format

        return cls

    return set_format
