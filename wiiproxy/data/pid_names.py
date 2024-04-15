from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(117)
@msp_data_struct_format('s', has_variable_size=True)
class PidNames(MultiWiiDataStructure):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
