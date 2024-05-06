from .  import _MspDataStructure, command_code, struct_format
from .. import MSP_PID

from typing import NoReturn

@command_code(MSP_PID)
@struct_format('30B')
class MspPid(_MspDataStructure):
    """Represents data values for the MSP_PID command."""
    pass
