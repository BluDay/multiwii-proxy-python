from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MotorPins(MultiWiiData):
    """
    Represents data values for the MSP_MOTOR_PINS command.
    """
    values: Final[Tuple[int]] = ()
