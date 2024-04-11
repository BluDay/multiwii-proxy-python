from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: Final[int] = 0

    satellites: Final[int] = 0

    coordinates: Final[Tuple[int]] = (0, 0)

    altitude: Final[int] = 0

    speed: Final[int] = 0

    ground_course: Final[int] = 0
