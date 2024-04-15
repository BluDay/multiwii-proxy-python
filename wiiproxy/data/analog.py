from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(110)
@msp_data_struct_format('B3H')
class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""

    voltage: int

    power_meter: int # Unclear

    rssi: int

    amperage: int
