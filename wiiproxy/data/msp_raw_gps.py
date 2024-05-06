from .  import _MspDataStructure, _Point2D, command_code, struct_format
from .. import MSP_RAW_GPS

from typing import NoReturn

@command_code(MSP_RAW_GPS)
@struct_format('2B2I3H')
class MspRawGps(_MspDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _fix: int

    _satellites: int

    _coordinates: _Point2D[float]

    _altitude: int

    _speed: int

    _ground_course: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._fix           = None
        self._satellites    = None
        self._coordinates   = None
        self._altitude      = None
        self._speed         = None
        self._ground_course = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def fix(self) -> int:
        """Gets the fix value."""
        return self._fix

    @property
    def satellites(self) -> int:
        """Gets the satellites value."""
        return self._satellites

    @property
    def coordinates(self) -> _Point2D[float]:
        """Gets the current coordinates."""
        return self._coordinates

    @property
    def altitude(self) -> int:
        """Gets the current altitude."""
        return self._altitude

    @property
    def speed(self) -> int:
        """Gets the current speed."""
        return self._speed

    @property
    def ground_course(self) -> int:
        """Gets the ground course value."""
        return self._ground_course

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
