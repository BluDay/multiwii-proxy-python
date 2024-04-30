from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_ALTITUDE

from typing import NoReturn

@command_code(MSP_ALTITUDE)
@struct_format('ih')
class Altitude(_MultiWiiData):
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

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        data = self._raw_data

        self._estimation = data[0]

        self._pressure_variation = data[1]
