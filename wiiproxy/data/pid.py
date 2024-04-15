from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.PID)
@MultiWiiDataStructure.struct_format('30B')
class Pid(MultiWiiDataStructure):
    """Represents data values for the MSP_PID command."""
    pass
