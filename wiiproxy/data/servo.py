from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.SERVO)
@MultiWiiDataStructure.struct_format('8H')
class Servo(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO command."""
    pass
