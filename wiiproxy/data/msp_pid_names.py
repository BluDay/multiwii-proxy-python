from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_PIDNAMES

from typing import NoReturn

@command_code(MSP_PIDNAMES)
@struct_format('s', has_variable_size=True)
class MspPidNames(_MspDataStructure):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
