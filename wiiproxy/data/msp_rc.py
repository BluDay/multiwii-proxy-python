from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_RC

from typing import NoReturn

@command_code(MSP_RC)
@struct_format('8H')
class MspRc(_MspDataStructure):
    """Represents data values for the MSP_RC command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _roll: int

    _pitch: int

    _yaw: int

    _throttle: int

    _aux: tuple[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._roll     = None
        self._pitch    = None
        self._yaw      = None
        self._throttle = None
        self._aux      = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def roll(self) -> int:
        """Gets the roll value."""
        return self._roll

    @property
    def pitch(self) -> int:
        """Gets the pitch value."""
        return self._pitch

    @property
    def yaw(self) -> int:
        """Gets the yaw value."""
        return self._yaw

    @property
    def throttle(self) -> int:
        """Gets the throttle value."""
        return self._throttle

    @property
    def aux(self) -> tuple[int]:
        """Gets the four auxillary values."""
        return self._aux

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        pass
