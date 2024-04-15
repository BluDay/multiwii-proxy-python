from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.SERVO_CONF)
@msp_data_struct_format('3HB', has_variable_size=True)
class ServoConf(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
