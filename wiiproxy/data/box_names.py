from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.BOXNAMES)
@MultiWiiDataStructure.struct_format('s', has_variable_size=True)
class BoxNames(MultiWiiDataStructure):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
