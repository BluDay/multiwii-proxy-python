from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.ANALOG)
@msp_data_struct_format('B3H')
class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""

    voltage: int

    power_meter: int # Unclear

    rssi: int

    amperage: int
