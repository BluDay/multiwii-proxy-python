from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Waypoint(_MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: Optional[int]

    position: Optional[tuple[int]]

    alt_hold: Optional[int]

    heading: Optional[int]

    time_to_stay: Optional[int]

    flag: Optional[int]
