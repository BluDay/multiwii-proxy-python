from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(120)
@msp_data_struct_format('3HB')
class ServoConf(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
