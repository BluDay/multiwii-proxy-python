from wiiproxy.config import (
    MultiWiiBox,
    MultiWiiCapability,
    MultiWiiMultitype
)

from dataclasses import dataclass
from typing      import Final, NoReturn

class _MultiWiiDataStructure(object):
    """Represents the base class for MSP data structure classes."""
    pass

@dataclass(slots=True)
class _MultiWiiDataIntegerValues(_MultiWiiDataStructure):
    """The base MultiWii class for data values with a single, public int tuple member."""
    values: Final[tuple[int] | None]

@dataclass(slots=True)
class _MultiWiiDataStringValues(_MultiWiiDataStructure):
    """The base class for data values with a single, public string tuple member."""
    values: Final[tuple[str] | None]

@dataclass(slots=True)
class Altitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: Final[int | None]

    pressure_variation: Final[int | None]

@dataclass(slots=True)
class Analog(_MultiWiiDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: Final[int | None]

    power_meter: Final[int | None] # Unclear

    rssi: Final[int | None]

    amperage: Final[int | None]

@dataclass(slots=True)
class Attitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Final[tuple[int] | None]

    heading: Final[int | None]

class Box(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_BOX command."""
    pass

@dataclass(slots=True)
class BoxIds(_MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Final[tuple[MultiWiiBox] | None]

class BoxNames(_MultiWiiDataStringValues):
    """Represents data values for the MSP_BOXNAMES command."""
    pass

@dataclass(slots=True)
class CompGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Final[int | None]

    direction_to_home: Final[int | None]

    update: Final[int | None] # What?

@dataclass(slots=True)
class Ident(_MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Final[float | None]

    multitype: Final[MultiWiiMultitype]

    capabilities: Final[tuple[MultiWiiCapability] | None]

    navi_version: Final[int | None]

@dataclass(slots=True)
class Misc(_MultiWiiDataStructure):
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
    fix: Final[int | None]

    satellites: Final[int | None]

    coordinates: Final[tuple[int] | None]

    altitude: Final[int | None]

    speed: Final[int | None]

    ground_course: Final[int | None]

@dataclass(slots=True)
class RawImu(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc:  Final[tuple[int] | None]
    gyro: Final[tuple[int] | None]
    mag:  Final[tuple[int] | None]

@dataclass(slots=True)
class Rc(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""
    roll:     Final[int | None]
    pitch:    Final[int | None]
    yaw:      Final[int | None]
    throttle: Final[int | None]

    aux: Final[tuple[int] | None]

@dataclass(slots=True)
class RcTuning(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""
    rate: Final[int | None]
    expo: Final[int | None]

    roll_pitch_rate: Final[int | None]

    yaw_rate: Final[int | None]

    dynamic_throttle_pid: Final[int | None]

    throttle_mid:  Final[int | None]
    throttle_expo: Final[int | None]

class Servo(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_SERVO command."""
    pass

class ServoConf(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_SERVO_CONF command."""
    pass

@dataclass(slots=True)
class Status(_MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: Final[int | None]

    i2c_errors: Final[int | None]

    sensors: Final[tuple[int] | None]

    flag: Final[int | None]

    global_conf: Final[int | None]

@dataclass(slots=True)
class Waypoint(_MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: Final[int | None]

    position: Final[tuple[int] | None]

    alt_hold: Final[int | None]

    heading: Final[int | None]

    time_to_stay: Final[int | None]

    flag: Final[int | None]

@dataclass(slots=True)
class MultiWiiDataValues(object):
    """Represents a collection of data values for all MultiWii structures."""
    ident:      Ident
    status:     Status
    raw_imu:    RawImu
    servo:      Servo
    servo_conf: ServoConf
    motor:      Motor
    motor_pins: MotorPins
    rc:         Rc
    rc_tuning:  RcTuning
    attitude:   Attitude
    altitude:   Altitude
    raw_gps:    RawGps
    comp_gps:   CompGps
    wp:         Waypoint
    analog:     Analog
    pid:        Pid
    pidnames:   PidNames
    box:        Box
    boxnames:   BoxNames
    boxids:     BoxIds
    misc:       Misc

    # ------------------------------------ INSTANCE METHODS ------------------------------------

    def reset_data(self) -> NoReturn:
        """Resets all data value instances. defines each field if not already defined."""
        self.ident      = Ident()
        self.status     = Status()
        self.raw_imu    = RawImu()
        self.servo      = Servo()
        self.servo_conf = ServoConf()
        self.motor      = Motor()
        self.motor_pins = MotorPins()
        self.rc         = Rc()
        self.rc_tuning  = RcTuning()
        self.attitude   = Attitude()
        self.altitude   = Altitude()
        self.raw_gps    = RawGps()
        self.comp_gps   = CompGps()
        self.wp         = Waypoint()
        self.analog     = Analog()
        self.pid        = Pid()
        self.pidnames   = PidNames()
        self.box        = Box()
        self.boxnames   = BoxNames()
        self.boxids     = BoxIds()
        self.misc       = Misc()
