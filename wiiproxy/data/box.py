from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.BOX)
@msp_data_struct_format('H', has_variable_size=True)
class Box(MultiWiiDataStructure):
    """Represents data values for the MSP_BOX command."""
    pass
