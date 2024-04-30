from .  import command_code, struct_format, MultiWiiData
from .. import MSP_PIDNAMES

from typing import NoReturn

@command_code(MSP_PIDNAMES)
@struct_format('s', has_variable_size=True)
class PidNames(MultiWiiData):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
