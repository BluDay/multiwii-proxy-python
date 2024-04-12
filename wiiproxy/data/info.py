from wiiproxy.config.capability import MultiWiiCapability
from wiiproxy.config.multitype  import MultiWiiMultitype
from wiiproxy.data._base        import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Analog(_MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: Optional[int]

    power_meter: Optional[int] # Unclear

    rssi: Optional[int]

    amperage: Optional[int]

@dataclass(slots=True)
class Ident(_MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Optional[float]

    multitype: Optional[MultiWiiMultitype]

    capabilities: Optional[tuple[MultiWiiCapability]]

    navi_version: Optional[int]

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

@dataclass(slots=True)
class Status(_MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: Optional[int]

    i2c_errors: Optional[int]

    sensors: Optional[tuple[int]]

    flag: Optional[int]

    global_conf: Optional[int]
