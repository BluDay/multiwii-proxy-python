from . import Point2D

from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.WP)
@MultiWiiDataStructure.struct_format('B3I2HB')
class Waypoint(MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""

    number: int

    position: Point2D

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
