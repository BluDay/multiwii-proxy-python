from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_SERVO

from typing import NoReturn

@command_code(MSP_SERVO)
@struct_format('8H')
class Servo(_MultiWiiData):
    """Represents data values for the MSP_SERVO command."""
    pass
