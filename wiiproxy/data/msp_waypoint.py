from .  import _MultiWiiData, _Point2D, command_code, struct_format
from .. import MSP_WP

from typing import NoReturn

@command_code(MSP_WP)
@struct_format('B3I2HB')
class MspWaypoint(_MultiWiiData):
    """Represents data values for the MSP_WP command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __number: int

    __position: _Point2D[float]

    __alt_hold: int

    __heading: int

    __time_to_stay: int

    __flag: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__number       = None
        self.__position     = None
        self.__alt_hold     = None
        self.__heading      = None
        self.__time_to_stay = None
        self.__flag         = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def number(self) -> int:
        """Gets the number value."""
        return self.__number

    @property
    def position(self) -> _Point2D[float]:
        """Gets a 2D point value of the current position."""
        return self.__position

    @property
    def alt_hold(self) -> int:
        """Gets the altitude hold value."""
        return self.__alt_hold

    @property
    def heading(self) -> int:
        """Gets the heading value."""
        return self.__heading

    @property
    def time_to_stay(self) -> int:
        """Gets the time-to-stay value."""
        return self.__time_to_stay

    @property
    def flag(self) -> int:
        """Gets the flag value."""
        return self.__flag

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
