from . import _MspValues, command_code, struct_format

from ..config       import MultiWiiBoxState
from ..msp_commands import MSP_BOX

from typing import NamedTuple, NoReturn

@command_code(MSP_BOX)
@struct_format('H', has_variable_size=True)
class MspBox(_MspValues):
    """Represents data values for the MSP_BOX command."""
    pass

class MspSetBoxItem(object):
    """Represents  for the MSP_SET_BOX command."""
    aux1: MultiWiiBoxState
    aux2: MultiWiiBoxState
    aux3: MultiWiiBoxState
    aux4: MultiWiiBoxState
     
    def compile(self) -> int:
        """Compiles all of the set box state values to a single unsigned integer value."""
        pass
