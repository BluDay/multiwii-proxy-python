from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Altitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: Final[int | None]

    pressure_variation: Final[int | None]
