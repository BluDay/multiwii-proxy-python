from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Final[Tuple[int] | None]

    heading: Final[int | None]
