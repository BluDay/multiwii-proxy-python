from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.PIDNAMES)
@msp_data_struct_format('s', has_variable_size=True)
class PidNames(MultiWiiDataStructure):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
