from ..config import (
    MultiWiiCapability,
    MultiWiiMultitype,
    MultiWiiSensor
)

from dataclasses import dataclass

@dataclass
class MspAnalog:
    """Represents data values for the MSP_ANALOG command."""
    voltage: float

    power_meter_sum: int

    rssi: int

    amperage: int

@dataclass
class MspIdent:
    """Represents data values for the MSP_IDENT command."""
    version: int

    multitype: MultiWiiMultitype

    capabilities: tuple[MultiWiiCapability]

    navi_version: int

@dataclass
class MspMisc:
    """Represents data values for the MSP_MISC command."""
    power_trigger: int

    throttle_failsafe: int

    throttle_idle: int

    throttle_min: int

    throttle_max: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: float

    battery_scale: int

    battery_warn_1: float

    battery_warn_2: float

    battery_critical: float

@dataclass
class MspSetMisc:
    """Represents data values for the MSP_SET_MISC command."""
    power_trigger: int

    throttle_min: int

    throttle_max: int

    min_command: int

    failsafe_throttle: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: float

    battery_scale: int

    battery_warn_1: float

    battery_warn_2: float

    battery_critical: float

@dataclass
class MspStatus:
    """Represents data values for the MSP_STATUS command."""
    cycle_time: int

    i2c_errors: int

    sensors: tuple[MultiWiiSensor]

    flag: int

    global_conf: int
