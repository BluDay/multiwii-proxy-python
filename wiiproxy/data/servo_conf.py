from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.SERVO_CONF)
@struct_format('3HB', has_variable_size=True)
class ServoConf(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
