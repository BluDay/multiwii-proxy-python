from . import command_code, struct_format, MultiWiiData, Point2D

from ..messaging import MspCommands

@command_code(MspCommands.ATTITUDE)
@struct_format('3h')
class Attitude(MultiWiiData):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D[float]

    heading: int
