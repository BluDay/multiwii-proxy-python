from . import Point2D

from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(108)
@msp_data_struct_format('3h')
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D

    heading: int
