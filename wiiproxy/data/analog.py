from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

@command_code(MspCommands.ANALOG)
@struct_format('B3H')
class Analog(MultiWiiData):
    """Represents data values for the MSP_ANALOG command."""

    voltage: int

    power_meter: int # Unclear

    rssi: int

    amperage: int
