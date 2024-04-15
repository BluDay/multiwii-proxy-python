from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.MOTOR)
@msp_data_struct_format('8H')
class Motor(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR command."""
    pass
