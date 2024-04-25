from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_MOTOR_PINS)
@struct_format('8B')
class MotorPins(MultiWiiData):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
