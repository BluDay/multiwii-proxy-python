from .base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Final[Tuple[int]] = (0, 0)

    heading: Final[int] = 0
