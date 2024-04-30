from .  import command_code, struct_format, MultiWiiData
from .. import MSP_BOXNAMES

from typing import NoReturn

@command_code(MSP_BOXNAMES)
@struct_format('s', has_variable_size=True)
class BoxNames(MultiWiiData):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
