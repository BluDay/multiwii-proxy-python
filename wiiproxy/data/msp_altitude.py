from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_ALTITUDE

from typing import NoReturn

@command_code(MSP_ALTITUDE)
@struct_format('ih')
class MspAltitude(_MultiWiiData):
    """Represents data values for the MSP_ALTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __estimation: int

    __pressure_variation: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__estimation         = None
        self.__pressure_variation = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def estimation(self) -> int:
        """Gets the estimation value."""
        return self.__estimation

    @property
    def pressure_variation(self) -> int:
        """Gets the pressure variation."""
        return self.__pressure_variation

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        data = self.__raw_data

        self.__estimation = data[0]

        self.__pressure_variation = data[1]
