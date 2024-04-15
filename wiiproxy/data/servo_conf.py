from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(120)
@msp_data_struct_format('3HB', has_variable_size=True)
class ServoConf(MultiWiiDataStructure):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass
