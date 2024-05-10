from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_SERVO

@command_code(MSP_SERVO)
@struct_format('8H')
class MspServo(_MspValues):
    """Represents data values for the MSP_SERVO command."""
    pass
