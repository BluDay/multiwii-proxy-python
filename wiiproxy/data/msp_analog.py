from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_ANALOG

from typing import NoReturn

@command_code(MSP_ANALOG)
@struct_format('B3H')
class MspAnalog(_MultiWiiData):
    """Represents data values for the MSP_ANALOG command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __voltage: int

    __power_meter: int # Unclear

    __rssi: int

    __amperage: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__voltage     = None
        self.__power_meter = None
        self.__rssi        = None
        self.__amperage    = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def voltage(self) -> int:
        """Gets the current voltage value."""
        return self.__voltage

    @property
    def power_meter(self) -> int:
        """Gets the power meter value."""
        return self.__power_meter

    @property
    def rssi(self) -> int:
        """Gets the rssi value."""
        return self.__rssi

    @property
    def amperage(self) -> int:
        """Gets the current amperage value."""
        return self.__amperage

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
