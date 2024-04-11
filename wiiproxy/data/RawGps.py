from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: Final[int | None]

    satellites: Final[int | None]

    coordinates: Final[Tuple[int] | None]

    altitude: Final[int | None]

    speed: Final[int | None]

    ground_course: Final[int | None]
