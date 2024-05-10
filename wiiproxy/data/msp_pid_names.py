from . import _MspNames, command_code, struct_format

from ..msp_commands import MSP_PIDNAMES

@command_code(MSP_PIDNAMES)
class MspPidNames(_MspNames):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
