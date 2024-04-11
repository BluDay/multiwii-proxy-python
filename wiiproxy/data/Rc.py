from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Rc(MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""
    roll:     Final[int | None]
    pitch:    Final[int | None]
    yaw:      Final[int | None]
    throttle: Final[int | None]

    aux: Final[Tuple[int] | None]
