from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_ANALOG)
@struct_format('B3H')
class Analog(MultiWiiData):
    """Represents data values for the MSP_ANALOG command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _voltage: int

    _power_meter: int # Unclear

    _rssi: int

    _amperage: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._voltage     = None
        self._power_meter = None
        self._rssi        = None
        self._amperage    = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def voltage(self) -> int:
        """Gets the current voltage value."""
        return self._voltage

    @property
    def power_meter(self) -> int:
        """Gets the power meter value."""
        return self._power_meter

    @property
    def rssi(self) -> int:
        """Gets the rssi value."""
        return self._rssi

    @property
    def amperage(self) -> int:
        """Gets the current amperage value."""
        return self._amperage

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
