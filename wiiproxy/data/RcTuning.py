from .base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RcTuning(MultiWiiDataStructure):
    """
    Represents data values for the MSP_RC_TUNING command.
    """
    rate: Final[int] = 0
    expo: Final[int] = 0

    roll_pitch_rate: Final[int] = 0

    yaw_rate: Final[int] = 0

    dynamic_throttle_pid: Final[int] = 0

    throttle_mid:  Final[int] = 0
    throttle_expo: Final[int] = 0
