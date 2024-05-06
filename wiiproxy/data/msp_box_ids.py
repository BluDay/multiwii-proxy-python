from . import _MspDataStructure, command_code, struct_format

from ..config       import MultiWiiBox
from ..msp_commands import MSP_BOXIDS

from typing import NoReturn

@command_code(MSP_BOXIDS)
@struct_format('B', has_variable_size=True)
class MspBoxIds(_MspDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    pass
