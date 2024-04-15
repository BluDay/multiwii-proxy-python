from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(115)
@msp_data_struct_format('8B')
class MotorPins(MultiWiiDataStructure):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass
