from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_MOTOR)
@struct_format('8H')
class Motor(MultiWiiData):
    """Represents data values for the MSP_MOTOR command."""
    pass
