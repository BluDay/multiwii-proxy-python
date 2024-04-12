from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class RawGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: Optional[int]

    satellites: Optional[int]

    coordinates: Optional[tuple[int]]

    altitude: Optional[int]

    speed: Optional[int]

    ground_course: Optional[int]
