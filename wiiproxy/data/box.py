from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.BOX)
@MultiWiiDataStructure.struct_format('H', has_variable_size=True)
class Box(MultiWiiDataStructure):
    """Represents data values for the MSP_BOX command."""
    pass
