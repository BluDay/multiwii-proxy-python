from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_PID

@command_code(MSP_PID)
@struct_format('30B')
class MspPid(_MspValues):
    """Represents data values for the MSP_PID command."""
    pass
