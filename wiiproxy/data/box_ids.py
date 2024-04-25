from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from ..config import MultiWiiBox

from typing import NoReturn

@command_code(MspCommands.MSP_BOXIDS)
@struct_format('B', has_variable_size=True)
class BoxIds(MultiWiiData):
    """Represents data values for the MSP_BOXIDS command."""
    pass
