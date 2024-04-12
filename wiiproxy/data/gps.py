from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class CompGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Optional[int]

    direction_to_home: Optional[int]

    update: Optional[int] # What?

@dataclass(slots=True)
class RawGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: Optional[int]

    satellites: Optional[int]

    coordinates: Optional[tuple[int]]

    altitude: Optional[int]

    speed: Optional[int]

    ground_course: Optional[int]

@dataclass(slots=True)
class Waypoint(_MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: Optional[int]

    position: Optional[tuple[int]]

    alt_hold: Optional[int]

    heading: Optional[int]

    time_to_stay: Optional[int]

    flag: Optional[int]
