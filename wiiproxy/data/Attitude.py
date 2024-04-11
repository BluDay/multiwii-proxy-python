from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Final[tuple[int] | None]

    heading: Final[int | None]
