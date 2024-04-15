from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.RC)
@msp_data_struct_format('8H')
class Rc(MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""

    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]
