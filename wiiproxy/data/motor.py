from .  import command_code, struct_format, MultiWiiData
from .. import MSP_MOTOR

from typing import NoReturn

@command_code(MSP_MOTOR)
@struct_format('8H')
class Motor(MultiWiiData):
    """Represents data values for the MSP_MOTOR command."""
    pass
