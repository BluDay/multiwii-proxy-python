from . import Point2D

from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(106)
@msp_data_struct_format('2B2I3H')
class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    fix: int

    satellites: int

    coordinates: Point2D

    altitude: int

    speed: int

    ground_course: int
