from .  import _MspDataStructure, command_code, struct_format
from .. import MSP_BOXNAMES

from typing import NoReturn

@command_code(MSP_BOXNAMES)
@struct_format('s', has_variable_size=True)
class MspBoxNames(_MspDataStructure):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
