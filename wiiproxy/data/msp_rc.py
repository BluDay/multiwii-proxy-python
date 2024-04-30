from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_RC

from typing import NoReturn

@command_code(MSP_RC)
@struct_format('8H')
class MspRc(_MultiWiiData):
    """Represents data values for the MSP_RC command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __roll: int

    __pitch: int

    __yaw: int

    __throttle: int

    __aux: tuple[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__roll     = None
        self.__pitch    = None
        self.__yaw      = None
        self.__throttle = None
        self.__aux      = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def roll(self) -> int:
        """Gets the roll value."""
        return self.__roll

    @property
    def pitch(self) -> int:
        """Gets the pitch value."""
        return self.__pitch

    @property
    def yaw(self) -> int:
        """Gets the yaw value."""
        return self.__yaw

    @property
    def throttle(self) -> int:
        """Gets the throttle value."""
        return self.__throttle

    @property
    def aux(self) -> tuple[int]:
        """Gets the four auxillary values."""
        return self.__aux

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
