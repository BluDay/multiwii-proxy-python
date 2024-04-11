from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RcTuning(MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""
    rate: Final[int | None]
    expo: Final[int | None]

    roll_pitch_rate: Final[int | None]

    yaw_rate: Final[int | None]

    dynamic_throttle_pid: Final[int | None]

    throttle_mid:  Final[int | None]
    throttle_expo: Final[int | None]
