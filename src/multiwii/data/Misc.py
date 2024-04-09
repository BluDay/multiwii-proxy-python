from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Misc(MultiWiiData):
    """
    Represents data values for the MSP_MISC command.
    """
    power_trigger: Final[int] = 0

    throttle_failsafe: Final[int] = 0
    throttle_idle:     Final[int] = 0
    throttle_min:      Final[int] = 0
    throttle_max:      Final[int] = 0

    plog_arm: Final[int] = 0

    plog_lifetime: Final[int] = 0

    mag_declination: Final[int] = 0

    battery_scale:    Final[int] = 0
    battery_warn_1:   Final[int] = 0
    battery_warn_2:   Final[int] = 0
    battery_critical: Final[int] = 0
