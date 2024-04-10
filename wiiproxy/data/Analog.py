from .base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: Final[int] = 0

    power_meter: Final[int] = 0 # Unclear

    rssi: Final[int] = 0

    amperage: Final[int] = 0
