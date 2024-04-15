from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.PIDNAMES)
@MultiWiiDataStructure.struct_format('s', has_variable_size=True)
class PidNames(MultiWiiDataStructure):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
