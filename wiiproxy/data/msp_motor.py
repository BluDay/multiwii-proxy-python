from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_MOTOR

@command_code(MSP_MOTOR)
@struct_format('8H')
class MspMotor(_MspValues):
    """Represents data values for the MSP_MOTOR command."""
    pass
