from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_COMP_GPS

from typing import NoReturn

@command_code(MSP_COMP_GPS)
@struct_format('2HB')
class MspCompGps(_MultiWiiData):
    """Represents data values for the MSP_COMP_GPS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __distance_to_home: int

    __direction_to_home: int

    __update: int # What?

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__distance_to_home  = None
        self.__direction_to_home = None
        self.__update            = None

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def distance_to_home(self) -> int:
        """Gets the distance to home value."""
        return self.__distance_to_home

    @property
    def direction_to_home(self) -> int:
        """Gets the direction to home value."""
        return self.__direction_to_home

    @property
    def update(self) -> int:
        """Gets the update value."""
        return self.__update

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
