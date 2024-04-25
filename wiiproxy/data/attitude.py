from . import command_code, struct_format, MultiWiiData, Point2D

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_ATTITUDE)
@struct_format('3h')
class Attitude(MultiWiiData):
    """Represents data values for the MSP_ATTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _angle: Point2D[float]

    _heading: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._angle   = None
        self._heading = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def angle(self) -> Point2D[float]:
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
