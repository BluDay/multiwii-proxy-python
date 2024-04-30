from .  import _MultiWiiData, _Point2D, command_code, struct_format
from .. import MSP_RAW_GPS

from typing import NoReturn

@command_code(MSP_RAW_GPS)
@struct_format('2B2I3H')
class MspRawGps(_MultiWiiData):
    """Represents data values for the MSP_RAW_GPS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __fix: int

    __satellites: int

    __coordinates: _Point2D[float]

    __altitude: int

    __speed: int

    __ground_course: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__fix           = None
        self.__satellites    = None
        self.__coordinates   = None
        self.__altitude      = None
        self.__speed         = None
        self.__ground_course = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def fix(self) -> int:
        """Gets the fix value."""
        return self.__fix

    @property
    def satellites(self) -> int:
        """Gets the satellites value."""
        return self.__satellites

    @property
    def coordinates(self) -> _Point2D[float]:
        """Gets the current coordinates."""
        return self.__coordinates

    @property
    def altitude(self) -> int:
        """Gets the current altitude."""
        return self.__altitude

    @property
    def speed(self) -> int:
        """Gets the current speed."""
        return self.__speed

    @property
    def ground_course(self) -> int:
        """Gets the ground course value."""
        return self.__ground_course

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
