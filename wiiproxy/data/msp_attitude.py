from .  import _MultiWiiData, _Point2D, command_code, struct_format
from .. import MSP_ATTITUDE

from typing import NoReturn

@command_code(MSP_ATTITUDE)
@struct_format('3h')
class MspAttitude(_MultiWiiData):
    """Represents data values for the MSP_ATTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __angle: _Point2D[float]

    __heading: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__angle   = None
        self.__heading = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def angle(self) -> _Point2D[float]:
        """Gets the angle values."""
        return self.__angle

    @property
    def heading(self) -> int:
        """Gets the heading value."""
        return self.__heading

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
