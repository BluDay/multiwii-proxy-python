from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Final[int | None]

    direction_to_home: Final[int | None]

    update: Final[int | None] # What?
