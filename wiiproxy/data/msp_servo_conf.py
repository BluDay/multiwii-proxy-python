from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_SERVO_CONF

@command_code(MSP_SERVO_CONF)
@struct_format('3HB', has_variable_size=True)
class MspServoConf(_MspValues):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
