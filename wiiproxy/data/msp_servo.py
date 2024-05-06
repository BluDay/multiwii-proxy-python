from .  import _MspDataStructure, command_code, struct_format
from .. import MSP_SERVO

from typing import NoReturn

@command_code(MSP_SERVO)
@struct_format('8H')
class MspServo(_MspDataStructure):
    """Represents data values for the MSP_SERVO command."""
    pass
