from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..config import MultiWiiBox

@msp_command_code(119)
@msp_data_struct_format('B')
class BoxIds(MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    pass
