from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_MOTOR_PINS

from typing import NoReturn

@command_code(MSP_MOTOR_PINS)
@struct_format('8B')
class MotorPins(_MultiWiiData):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
