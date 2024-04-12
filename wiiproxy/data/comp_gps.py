from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class CompGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Optional[int]

    direction_to_home: Optional[int]

    update: Optional[int] # What?
