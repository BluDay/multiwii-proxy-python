from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_BOXNAMES)
@struct_format('s', has_variable_size=True)
class BoxNames(MultiWiiData):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
