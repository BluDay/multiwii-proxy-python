from ..config import MultiWiiCapability, MultiWiiMultitype, MultiWiiSensor

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspAnalog:
    """Represents data values for the MSP_ANALOG command."""
    voltage: float

    power_meter_sum: int

    rssi: int

    amperage: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            voltage=data[0] / 10.0,
            power_meter_sum=data[1],
            rssi=data[2],
            amperage=data[3]
        )

@dataclass
class MspIdent:
    """Represents data values for the MSP_IDENT command."""
    version: int

    multitype: MultiWiiMultitype

    capabilities: tuple[MultiWiiCapability]

    navi_version: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            version=data[0],
            multitype=MultiWiiMultitype(data[1]),
            capabilities=MultiWiiCapability.get_capabilities(data[2]),
            navi_version=data[3]
        )

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

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            power_trigger=data[0],
            throttle_failsafe=data[1],
            throttle_idle=data[2],
            throttle_min=data[3],
            throttle_max=data[4],
            plog_arm=data[5],
            plog_lifetime=data[6],
            mag_declination=data[7] / 10.0,
            battery_scale=data[8],
            battery_warn_1=data[9] / 10.0,
            battery_warn_2=data[10] / 10.0,
            battery_critical=data[11] / 10.0
        )

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

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            cycle_time=data[0],
            i2c_errors=data[1],
            sensors=(),
            flag=data[3],
            global_conf=data[4]
        )
