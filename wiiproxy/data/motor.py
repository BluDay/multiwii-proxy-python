from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_MOTOR

from typing import NoReturn

@command_code(MSP_MOTOR)
@struct_format('8H')
class Motor(_MultiWiiData):
    """Represents data values for the MSP_MOTOR command."""
    pass
