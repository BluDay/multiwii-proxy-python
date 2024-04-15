from . import Point2D

from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.RAW_GPS)
@MultiWiiDataStructure.struct_format('2B2I3H')
class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    fix: int

    satellites: int

    coordinates: Point2D

    altitude: int

    speed: int

    ground_course: int
