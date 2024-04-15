from . import Point2D

from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.RAW_GPS)
@struct_format('2B2I3H')
class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    fix: int

    satellites: int

    coordinates: Point2D

    altitude: int

    speed: int

    ground_course: int
