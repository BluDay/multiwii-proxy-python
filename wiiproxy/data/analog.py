from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.ANALOG)
@struct_format('B3H')
class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""

    voltage: int

    power_meter: int # Unclear

    rssi: int

    amperage: int
