from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(101)
@msp_data_struct_format('3HIB')
class Status(MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""

    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int
