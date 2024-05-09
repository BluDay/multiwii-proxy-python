from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_ANALOG

from typing import NoReturn

@command_code(MSP_ANALOG)
@struct_format('B3H')
class MspAnalog(_MspDataStructure):
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

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        pass
