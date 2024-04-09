from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Servo(MultiWiiData):
    """
    Represents data values for the MSP_SERVO command.
    """
    values: Final[Tuple[int]] = ()
