from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(107)
@msp_data_struct_format('2HB')
class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""

    distance_to_home: int

    direction_to_home: int

    update: int # What?
