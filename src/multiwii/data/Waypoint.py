from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Waypoint(MultiWiiData):
    """
    Represents data values for the MSP_WP command.
    """
    number: Final[int] = 0

    position: Final[Tuple[int]] = (0, 0)

    alt_hold: Final[int] = 0

    heading: Final[int] = 0

    time_to_stay: Final[int] = 0

    flag: Final[int] = 0
