from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

from typing import NoReturn

@command_code(MspCommands.STATUS)
@struct_format('3HIB')
class Status(MultiWiiData):
    """Represents data values for the MSP_STATUS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _cycle_time: int

    _i2c_errors: int

    _sensors: tuple[int]

    _flag: int

    _global_conf: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._cycle_time  = None
        self._i2c_errors  = None
        self._sensors     = None
        self._flag        = None
        self._global_conf = None

    # -------------------------------------- PROPERTIES ----------------------------------------
    
    @property
    def cycle_time(self) -> int:
        """Gets the cycle time value."""
        return self._cycle_time

    @property
    def i2c_errors(self) -> int:
        """Gets the I2C errors value."""
        return self._i2c_errors

    @property
    def sensors(self) -> tuple[int]:
        """Gets a list of available sensors."""
        return self._sensors

    @property
    def flag(self) -> int:
        """Gets the flag value."""
        return self._flag

    @property
    def global_conf(self) -> int:
        """Gets the global conf value."""
        return self._global_conf

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
