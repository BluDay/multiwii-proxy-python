from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.SERVO)
@struct_format('8H')
class Servo(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO command."""
    pass
