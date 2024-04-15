from . import Point2D

from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.ATTITUDE)
@struct_format('3h')
class Attitude(MultiWiiData):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D[float]

    heading: int
