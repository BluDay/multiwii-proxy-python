from . import Point2D

from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.ATTITUDE)
@MultiWiiDataStructure.struct_format('3h')
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D

    heading: int
