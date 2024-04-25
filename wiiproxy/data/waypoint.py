from . import command_code, struct_format, MultiWiiData, Point2D

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_WP)
@struct_format('B3I2HB')
class Waypoint(MultiWiiData):
    """Represents data values for the MSP_WP command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _number: int

    _position: Point2D[float]

    _alt_hold: int

    _heading: int

    _time_to_stay: int

    _flag: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._number       = None
        self._position     = None
        self._alt_hold     = None
        self._heading      = None
        self._time_to_stay = None
        self._flag         = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def number(self) -> int:
        """Gets the number value."""
        return self._number

    @property
    def position(self) -> Point2D[float]:
        """Gets a 2D point value of the current position."""
        return self._position

    @property
    def alt_hold(self) -> int:
        """Gets the altitude hold value."""
        return self._alt_hold

    @property
    def heading(self) -> int:
        """Gets the heading value."""
        return self._heading

    @property
    def time_to_stay(self) -> int:
        """Gets the time-to-stay value."""
        return self._time_to_stay

    @property
    def flag(self) -> int:
        """Gets the flag value."""
        return self._flag

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
