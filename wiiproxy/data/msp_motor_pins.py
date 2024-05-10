from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_MOTOR_PINS

from typing import NoReturn

@command_code(MSP_MOTOR_PINS)
@struct_format('8B')
class MspMotorPins(_MspValues):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
