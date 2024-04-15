from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.RC)
@struct_format('8H')
class Rc(MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""

    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]
