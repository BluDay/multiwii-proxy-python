from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_SERVO)
@struct_format('8H')
class Servo(MultiWiiData):
    """Represents data values for the MSP_SERVO command."""
    pass
