from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_STATUS

from typing import NoReturn

@command_code(MSP_STATUS)
@struct_format('3HIB')
class MspStatus(_MultiWiiData):
    """Represents data values for the MSP_STATUS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __cycle_time: int

    __i2c_errors: int

    __sensors: tuple[int]

    __flag: int

    __global_conf: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__cycle_time  = None
        self.__i2c_errors  = None
        self.__sensors     = None
        self.__flag        = None
        self.__global_conf = None

    # -------------------------------------- PROPERTIES ----------------------------------------
    
    @property
    def cycle_time(self) -> int:
        """Gets the cycle time value."""
        return self.__cycle_time

    @property
    def i2c_errors(self) -> int:
        """Gets the I2C errors value."""
        return self.__i2c_errors

    @property
    def sensors(self) -> tuple[int]:
        """Gets a list of available sensors."""
        return self.__sensors

    @property
    def flag(self) -> int:
        """Gets the flag value."""
        return self.__flag

    @property
    def global_conf(self) -> int:
        """Gets the global conf value."""
        return self.__global_conf

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
