from abc    import ABC, abstractmethod
from typing import Callable, Final, NoReturn, Type

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

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int]

    HAS_VARIABLE_SIZE: Final[bool]

    STRUCT_FORMAT: Final[str]

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    @abstractmethod
    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        pass

@struct_format('s', has_variable_size=True)
class _MspNames(_MspDataStructure):
    """Represents a class for storing decoded and separated MSP name values."""

    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    NAME_SEPARATION_CHAR: Final[str] = ';'
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _names: tuple[str]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._names = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def names(self) -> tuple[str]:
        """Gets the names."""
        return self._names

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._names = tuple(data[0].decode().split(_MspNames.NAME_SPARATION_CHAR))

class _MspValues(_MspDataStructure):
    """Represents a class for storing unserialized MSP values."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _values: tuple[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._values = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def values(self) -> tuple[int]:
        """Gets the values."""
        return self._values

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._values = data
