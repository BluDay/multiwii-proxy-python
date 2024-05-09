from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_BOX

from typing import NoReturn

@command_code(MSP_BOX)
@struct_format('H', has_variable_size=True)
class MspBox(_MspDataStructure):
    """Represents data values for the MSP_BOX command."""

    """
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _values: tuple[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        \"""Initializes a new instance with default values.\"""
        self._values = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def values(self) -> tuple[int]:
        \"""Gets the main values.\"""
        return self._values

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        \"""Updates the current values by unserialized data values.\"""
        pass
    """
    pass
