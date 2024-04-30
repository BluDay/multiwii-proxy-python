from .  import command_code, struct_format, MultiWiiData
from .. import MSP_BOXIDS

from ..config import MultiWiiBox

from typing import NoReturn

@command_code(MSP_BOXIDS)
@struct_format('B', has_variable_size=True)
class BoxIds(MultiWiiData):
    """Represents data values for the MSP_BOXIDS command."""
    pass
