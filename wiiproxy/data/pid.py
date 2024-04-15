from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.PID)
@msp_data_struct_format('30B')
class Pid(MultiWiiDataStructure):
    """Represents data values for the MSP_PID command."""
    pass
