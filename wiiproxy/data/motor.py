from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.MOTOR)
@struct_format('8H')
class Motor(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR command."""
    pass
