from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Analog(_MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: Optional[int]

    power_meter: Optional[int] # Unclear

    rssi: Optional[int]

    amperage: Optional[int]
