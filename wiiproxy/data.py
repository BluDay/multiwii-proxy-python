from wiiproxy.config import (
    MultiWiiBox,
    MultiWiiCapability,
    MultiWiiMultitype
)

from dataclasses import dataclass
from typing      import NoReturn, Optional

class _MultiWiiDataStructure(object):
    """Represents the base class for MSP data structure classes."""
    pass

@dataclass(slots=True)
class _MultiWiiDataIntegerValues(_MultiWiiDataStructure):
    """The base MultiWii class for data values with a single, public int tuple member."""
    values: Optional[tuple[int]]

@dataclass(slots=True)
class _MultiWiiDataStringValues(_MultiWiiDataStructure):
    """The base class for data values with a single, public string tuple member."""
    values: Optional[tuple[str]]

@dataclass(slots=True)
class Altitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: Optional[int]

    pressure_variation: Optional[int]

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

@dataclass(slots=True)
class MultiWiiDataValues(object):
    """Represents a collection of data values for all MultiWii structures."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

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

    def _reset_data(self) -> NoReturn:
        """Resets all data value instances. defines each field if not already defined."""
        self.ident = Ident(
            version=None,
            multitype=None,
            capabilities=None,
            navi_version=None
        )

        self.status = Status(
            cycle_time=None,
            i2c_errors=None,
            sensors=None,
            flag=None,
            global_conf=None
        )

        self.raw_imu = RawImu(acc=None, gyro=None, mag=None)

        self.servo = Servo(values=None)

        self.servo_conf = ServoConf(values=None)

        self.motor = Motor(values=None)

        self.motor_pins = MotorPins(values=None)

        self.rc = Rc(
		    roll=None,
            pitch=None,
            yaw=None,
            throttle=None,
            aux=None
		)

        self.rc_tuning = RcTuning(
		    rate=None,
            expo=None,
            roll_pitch_rate=None,
            yaw_rate=None,
            dynamic_throttle_pid=None,
            throttle_mid=None,
            throttle_expo=None
		)

        self.attitude = Attitude(angle=None, heading=None)

        self.altitude = Altitude(
            estimation=None,
            pressure_variation=None
        )

        self.raw_gps = RawGps(
		    fix=None,
            satellites=None,
            coordinates=None,
            altitude=None,
            speed=None,
            ground_course=None
		)

        self.comp_gps = CompGps(
		    distance_to_home=None,
		    direction_to_home=None,
            update=None
		)

        self.wp = Waypoint(
	        number=None,
            position=None,
            alt_hold=None,
            heading=None,
            time_to_stay=None,
            flag=None
		)

        self.analog = Analog(
		    voltage=None,
            power_meter=None,
            rssi=None,
            amperage=None
		)

        self.pid = Pid(values=None)

        self.pidnames = PidNames(values=None)

        self.box = Box(values=None)

        self.boxnames = BoxNames(values=None)

        self.boxids = BoxIds(values=None)

        self.misc = Misc(
		    power_trigger=None,
            throttle_failsafe=None,
            throttle_idle=None,
            throttle_min=None,
            throttle_max=None,
            plog_arm=None,
            plog_lifetime=None,
            mag_declination=None,
            battery_scale=None,
            battery_warn_1=None,
            battery_warn_2=None,
            battery_critical=None
		)
