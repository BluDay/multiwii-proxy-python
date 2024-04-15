from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.MOTOR_PINS)
@MultiWiiDataStructure.struct_format('8B')
class MotorPins(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
