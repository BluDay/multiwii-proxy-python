from . import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class RcTuning(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""
    rate: Optional[int]
    expo: Optional[int]

    roll_pitch_rate: Optional[int]

    yaw_rate: Optional[int]

    dynamic_throttle_pid: Optional[int]

    throttle_mid:  Optional[int]
    throttle_expo: Optional[int]
