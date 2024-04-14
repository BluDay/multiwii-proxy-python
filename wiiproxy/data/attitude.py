from . import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Attitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Optional[tuple[int]]

    heading: Optional[int]
