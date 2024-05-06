from .  import _MspDataStructure, _Point2D, command_code, struct_format
from .. import MSP_ATTITUDE

from typing import NoReturn

@command_code(MSP_ATTITUDE)
@struct_format('3h')
class MspAttitude(_MspDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _angle: _Point2D[float]

    _heading: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._angle   = None
        self._heading = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def angle(self) -> _Point2D[float]:
        """Gets the angle values."""
        return self._angle

    @property
    def heading(self) -> int:
        """Gets the heading value."""
        return self._heading

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
