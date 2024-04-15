from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.COMP_GPS)
@msp_data_struct_format('2HB')
class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""

    distance_to_home: int

    direction_to_home: int

    update: int # What?
