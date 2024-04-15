from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

from typing import NoReturn

@command_code(MspCommands.PIDNAMES)
@struct_format('s', has_variable_size=True)
class PidNames(MultiWiiData):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
