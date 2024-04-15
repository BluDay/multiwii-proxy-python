from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.MOTOR_PINS)
@struct_format('8B')
class MotorPins(MultiWiiData):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
