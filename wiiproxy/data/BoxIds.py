from wiiproxy.config                          import MultiWiiBox
from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class BoxIds(MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Final[Tuple[MultiWiiBox] | None]
