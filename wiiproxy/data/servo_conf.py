from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.SERVO_CONF)
@MultiWiiDataStructure.struct_format('3HB', has_variable_size=True)
class ServoConf(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
