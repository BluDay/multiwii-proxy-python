from . import command_code, struct_format, MultiWiiData

from ..config    import MultiWiiBox
from ..messaging import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_BOXIDS)
@struct_format('B', has_variable_size=True)
class BoxIds(MultiWiiData):
    """Represents data values for the MSP_BOXIDS command."""
    pass
