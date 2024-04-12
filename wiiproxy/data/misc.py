from wiiproxy.data._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Misc(_MultiWiiDataStructure):
    """Represents data values for the MSP_MISC command."""
    power_trigger: Optional[int]

    throttle_failsafe: Optional[int]

    throttle_idle: Optional[int]

    throttle_min: Optional[int]

    throttle_max: Optional[int]

    plog_arm: Optional[int]

    plog_lifetime: Optional[int]

    mag_declination: Optional[int]

    battery_scale: Optional[int]

    battery_warn_1: Optional[int]

    battery_warn_2: Optional[int]

    battery_critical: Optional[int]
