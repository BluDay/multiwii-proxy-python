from ._base import MultiWiiDataStructure

class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""

    voltage: int

    power_meter: int # Unclear

    rssi: int

    amperage: int
