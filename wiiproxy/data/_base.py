from abc    import ABC, abstractmethod
from typing import Any, Callable, Final, NoReturn, Self, Type

def command_code(value: int) -> Callable[[int], Type]:
    """Decorator for setting the command code of a data structure."""
    def apply(cls: Type) -> Type:
        cls.COMMAND_CODE = value

        return cls

    return apply

def struct_format(value: str, has_variable_size: bool = False) -> Callable[[str], Type]:
    """Decorator for setting the struct format for data values."""
    def apply(cls: Type) -> Type:
        cls.STRUCT_FORMAT = value

        cls.HAS_VARIABLE_SIZE = has_variable_size

        return cls

    return apply

class _MspDataStructure(ABC):
    """Represents the base class for MSP data structure classes."""
    COMMAND_CODE: Final[int]

    HAS_VARIABLE_SIZE: Final[bool]

    STRUCT_FORMAT: Final[str]

    @staticmethod
    @abstractmethod
    def parse(data: tuple) -> Any:
        """Updates the current values by unserialized data values."""
        pass

@struct_format('s', has_variable_size=True)
class _MspNames(_MspDataStructure):
    """Represents a class for storing decoded and separated MSP name values."""
    NAME_SEPARATION_CHAR: Final[str] = ';'
    
    names: tuple[str]

    @staticmethod
    def parse(data: tuple) -> Any:
        """Updates the current values by unserialized data values."""
        return tuple(data[0].decode().split(_MspNames.NAME_SPARATION_CHAR))

class _MspValues(_MspDataStructure):
    """Represents a class for storing unserialized MSP values."""
    _values: tuple[int]

    @staticmethod
    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        return data
