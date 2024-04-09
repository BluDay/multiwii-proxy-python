from .base import MspDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Rc(MspDataStructure):
    """
    Represents data values for the MSP_RC command.
    """
    roll:     Final[int] = 0
    pitch:    Final[int] = 0
    yaw:      Final[int] = 0
    throttle: Final[int] = 0

    aux: Final[Tuple[int]] = (0, 0, 0, 0)
