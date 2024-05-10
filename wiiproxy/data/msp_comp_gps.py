from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_COMP_GPS

from typing import NoReturn

@command_code(MSP_COMP_GPS)
@struct_format('2HB')
class MspCompGps(_MspDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _distance_to_home: int

    _direction_to_home: int

    _update: int # What?

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._distance_to_home  = None
        self._direction_to_home = None
        self._update            = None

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def distance_to_home(self) -> int:
        """Gets the distance to home value."""
        return self._distance_to_home

    @property
    def direction_to_home(self) -> int:
        """Gets the direction to home value."""
        return self._direction_to_home

    @property
    def update(self) -> int:
        """Gets the update value."""
        return self._update

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._distance_to_home  = data[0]
        self._direction_to_home = data[1]
        self._update            = data[2]
