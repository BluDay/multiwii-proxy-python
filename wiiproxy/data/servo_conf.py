from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_SERVO_CONF

from typing import NoReturn

@command_code(MSP_SERVO_CONF)
@struct_format('3HB', has_variable_size=True)
class ServoConf(_MultiWiiData):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
