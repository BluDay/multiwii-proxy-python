from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.PID)
@struct_format('30B')
class Pid(MultiWiiDataStructure):
    """Represents data values for the MSP_PID command."""
    pass
