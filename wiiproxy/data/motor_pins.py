from .  import command_code, struct_format, MultiWiiData
from .. import MSP_MOTOR_PINS

from typing import NoReturn

@command_code(MSP_MOTOR_PINS)
@struct_format('8B')
class MotorPins(MultiWiiData):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
