from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_ALTITUDE

from typing import NoReturn

@command_code(MSP_ALTITUDE)
@struct_format('ih')
class MspAltitude(_MspDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _estimation: int

    _pressure_variation: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._estimation         = None
        self._pressure_variation = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def estimation(self) -> int:
        """Gets the estimation value."""
        return self._estimation

    @property
    def pressure_variation(self) -> int:
        """Gets the pressure variation."""
        return self._pressure_variation

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update_values(self, raw_data: bytes) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        self._estimation = raw_data[0]

        self._pressure_variation = raw_data[1]
