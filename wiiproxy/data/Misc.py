from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Misc(MultiWiiDataStructure):
    """Represents data values for the MSP_MISC command."""
    power_trigger: Final[int | None]

    throttle_failsafe: Final[int | None]
    throttle_idle:     Final[int | None]
    throttle_min:      Final[int | None]
    throttle_max:      Final[int | None]

    plog_arm:      Final[int | None]
    plog_lifetime: Final[int | None]

    mag_declination: Final[int | None]

    battery_scale:    Final[int | None]
    battery_warn_1:   Final[int | None]
    battery_warn_2:   Final[int | None]
    battery_critical: Final[int | None]
