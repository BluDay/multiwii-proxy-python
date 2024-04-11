from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Waypoint(MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: Final[int | None]

    position: Final[Tuple[int] | None]

    alt_hold: Final[int | None]

    heading: Final[int | None]

    time_to_stay: Final[int | None]

    flag: Final[int | None]
