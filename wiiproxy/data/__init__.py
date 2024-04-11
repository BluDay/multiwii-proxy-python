from wiiproxy.config import (
    MultiWiiBox,
    MultiWiiCapability,
    MultiWiiMultitype
)

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
class Attitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Optional[tuple[int]]

    heading: Optional[int]

class Box(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_BOX command."""
    pass

@dataclass(slots=True)
class BoxIds(_MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Optional[tuple[MultiWiiBox]]

class BoxNames(_MultiWiiDataStringValues):
    """Represents data values for the MSP_BOXNAMES command."""
    pass

@dataclass(slots=True)
class CompGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Optional[int]

    direction_to_home: Optional[int]

    update: Optional[int] # What?

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
    throttle_idle:     Optional[int]
    throttle_min:      Optional[int]
    throttle_max:      Optional[int]

    plog_arm:      Optional[int]
    plog_lifetime: Optional[int]

    mag_declination: Optional[int]

    battery_scale:    Optional[int]
    battery_warn_1:   Optional[int]
    battery_warn_2:   Optional[int]
    battery_critical: Optional[int]

class Motor(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_MOTOR command."""
    pass

class MotorPins(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_MOTOR_PINS command."""
    pass

class Pid(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_PID command."""
    pass

class PidNames(_MultiWiiDataStringValues):
    """Represents data values for the MSP_PIDNAMES command."""
    pass

@dataclass(slots=True)
class RawGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: Optional[int]

    satellites: Optional[int]

    coordinates: Optional[tuple[int]]

    altitude: Optional[int]

    speed: Optional[int]

    ground_course: Optional[int]

@dataclass(slots=True)
class RawImu(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc:  Optional[tuple[int]]
    gyro: Optional[tuple[int]]
    mag:  Optional[tuple[int]]

@dataclass(slots=True)
class Rc(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""
    roll:     Optional[int]
    pitch:    Optional[int]
    yaw:      Optional[int]
    throttle: Optional[int]

    aux: Optional[tuple[int]]

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

class Servo(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_SERVO command."""
    pass

class ServoConf(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass

@dataclass(slots=True)
class Status(_MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: Optional[int]

    i2c_errors: Optional[int]

    sensors: Optional[tuple[int]]

    flag: Optional[int]

    global_conf: Optional[int]

@dataclass(slots=True)
class Waypoint(_MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: Optional[int]

    position: Optional[tuple[int]]

    alt_hold: Optional[int]

    heading: Optional[int]

    time_to_stay: Optional[int]

    flag: Optional[int]
