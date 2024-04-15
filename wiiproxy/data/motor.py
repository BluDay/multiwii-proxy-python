from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(104)
@msp_data_struct_format('8H')
class Motor(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR command."""
    pass
