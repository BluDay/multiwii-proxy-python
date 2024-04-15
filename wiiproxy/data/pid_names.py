from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.PIDNAMES)
@struct_format('s', has_variable_size=True)
class PidNames(MultiWiiDataStructure):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
