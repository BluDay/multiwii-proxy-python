from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(103)
@msp_data_struct_format('8H')
class Servo(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO command."""
    pass
