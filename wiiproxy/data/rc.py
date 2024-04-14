from ._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Rc(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""
    roll: Optional[int]

    pitch: Optional[int]

    yaw: Optional[int]

    throttle: Optional[int]

    aux: Optional[tuple[int]]
