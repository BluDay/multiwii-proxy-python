from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

from typing import NoReturn

@command_code(MspCommands.MOTOR)
@struct_format('8H')
class Motor(MultiWiiData):
    """Represents data values for the MSP_MOTOR command."""
    pass
