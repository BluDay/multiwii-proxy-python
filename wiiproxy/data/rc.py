from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.RC)
@MultiWiiDataStructure.struct_format('8H')
class Rc(MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""

    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]
