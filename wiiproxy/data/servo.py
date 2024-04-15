from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.SERVO)
@msp_data_struct_format('8H')
class Servo(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO command."""
    pass
