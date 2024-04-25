from . import command_code, struct_format, MultiWiiData

from .. import MspCommands

from typing import NoReturn

@command_code(MspCommands.MSP_SERVO_CONF)
@struct_format('3HB', has_variable_size=True)
class ServoConf(MultiWiiData):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
