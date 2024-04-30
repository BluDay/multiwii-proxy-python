from .  import command_code, struct_format, MultiWiiData
from .. import MSP_PID

from typing import NoReturn

@command_code(MSP_PID)
@struct_format('30B')
class Pid(MultiWiiData):
    """Represents data values for the MSP_PID command."""
    pass
