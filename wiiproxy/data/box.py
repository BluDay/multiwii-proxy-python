from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(113)
@msp_data_struct_format('H', has_variable_size=True)
class Box(MultiWiiDataStructure):
    """Represents data values for the MSP_BOX command."""
    pass
