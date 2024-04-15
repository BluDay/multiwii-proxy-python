from . import Point2D

from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(118)
@msp_data_struct_format('B3I2HB')
class Waypoint(MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""

    number: int

    position: Point2D

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
