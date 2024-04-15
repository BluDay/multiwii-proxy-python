from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.MOTOR)
@struct_format('8H')
class Motor(MultiWiiData):
    """Represents data values for the MSP_MOTOR command."""
    pass
