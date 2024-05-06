from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_MOTOR

from typing import NoReturn

@command_code(MSP_MOTOR)
@struct_format('8H')
class MspMotor(_MspDataStructure):
    """Represents data values for the MSP_MOTOR command."""
    pass
