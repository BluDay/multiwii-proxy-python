from . import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Altitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: Optional[int]

    pressure_variation: Optional[int]
