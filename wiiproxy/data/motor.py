from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.MOTOR)
@MultiWiiDataStructure.struct_format('8H')
class Motor(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR command."""
    pass
