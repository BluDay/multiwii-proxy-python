from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.BOX)
@struct_format('H', has_variable_size=True)
class Box(MultiWiiData):
    """Represents data values for the MSP_BOX command."""
    pass
