from . import Point2D

from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.ATTITUDE)
@struct_format('3h')
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D

    heading: int
