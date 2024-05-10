from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_BOX

from typing import NamedTuple

@command_code(MSP_BOX)
@struct_format('H', has_variable_size=True)
class MspBox(_MspValues):
    """Represents data values for the MSP_BOX command."""
    pass

class MspSetBoxItem(object):
    """Represents  for the MSP_SET_BOX command."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _aux1: MultiWiiBoxState
    _aux2: MultiWiiBoxState
    _aux3: MultiWiiBoxState
    _aux4: MultiWiiBoxState
     
    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._aux1 = None
        self._aux2 = None
        self._aux3 = None
        self._aux4 = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def aux1(self) -> MultiWiiBoxState:
        """Gets the box state value for aux 1."""
        return self._aux1

    @property
    def aux2(self) -> MultiWiiBoxState:
        """Gets the box state value for aux 2."""
        return self._aux2

    @property
    def aux3(self) -> MultiWiiBoxState:
        """Gets the box state value for aux 3."""
        return self._aux3

    @property
    def aux4(self) -> MultiWiiBoxState:
        """Gets the box state value for aux 4."""
        return self._aux4

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def compile(self) -> int:
        """Compiles all of the set box state values to a single unsigned integer value."""
        pass
