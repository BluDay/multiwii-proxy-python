from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Altitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: Final[int] = 0

    pressure_variation: Final[int] = 0
