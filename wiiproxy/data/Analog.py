from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Analog(MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: Final[int | None]

    power_meter: Final[int | None] # Unclear

    rssi: Final[int | None]

    amperage: Final[int | None]
