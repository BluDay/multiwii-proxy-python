from ._base import MultiWiiDataStructure

from ..config                 import MultiWiiBox
from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.BOXIDS)
@MultiWiiDataStructure.struct_format('B', has_variable_size=True)
class BoxIds(MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    pass
