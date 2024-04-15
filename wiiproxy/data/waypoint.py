from . import Point2D

from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.WP)
@struct_format('B3I2HB')
class Waypoint(MultiWiiData):
    """Represents data values for the MSP_WP command."""

    number: int

    position: Point2D[float]

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
