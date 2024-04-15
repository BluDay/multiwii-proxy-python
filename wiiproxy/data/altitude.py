from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

from typing import NoReturn

@MultiWiiDataStructure.command_code(MspCommands.ALTITUDE)
@MultiWiiDataStructure.struct_format('ih')
class Altitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _estimation: int

    _pressure_variation: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._estimation         = None
        self._pressure_variation = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def estimation(self) -> int:
        """Gets the estimation value."""
        return self._estimation

    @property
    def pressure_variation(self) -> int:
        """Gets the pressure variation."""
        return self._pressure_variation

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(data: bytes) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        self._estimation = data[0] # int32

        self._pressure_variation = data[1] # int16
