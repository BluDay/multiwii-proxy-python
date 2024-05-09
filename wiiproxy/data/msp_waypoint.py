from . import _MspDataStructure, _Point2D, command_code, struct_format

from ..msp_commands import MSP_WP

from typing import NoReturn

@command_code(MSP_WP)
@struct_format('B3I2HB')
class MspWaypoint(_MspDataStructure):
    """Represents data values for the MSP_WP command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _number: int

    _position: _Point2D[float]

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
    def position(self) -> _Point2D[float]:
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

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        pass
