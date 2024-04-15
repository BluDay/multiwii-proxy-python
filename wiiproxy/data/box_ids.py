from ._base import command_code, struct_format, MultiWiiDataStructure

from ..config                 import MultiWiiBox
from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.BOXIDS)
@struct_format('B', has_variable_size=True)
class BoxIds(MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    pass
