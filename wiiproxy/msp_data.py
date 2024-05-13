from .msp_config import (
    MultiWiiBox,
    MultiWiiBoxState,
    MultiWiiCapability,
    MultiWiiMultitype
)

from dataclasses import dataclass

@dataclass
class MspAltitude:
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: int

    pressure_variation: int

@dataclass
class MspAnalog:
    """Represents data values for the MSP_ANALOG command."""
    voltage: int

    power_meter_sum: int

    rssi: int

    amperage: int

@dataclass
class MspAttitude:
    """Represents data values for the MSP_ATTITUDE command."""
    angle_x: float
    angle_y: float

    heading: int

@dataclass
class MspBox:
    """Represents data values for the MSP_BOX command."""
    values: tuple[int]

@dataclass
class MspBoxIds:
    """Represents data values for the MSP_BOXIDS command."""
    values: tuple[MultiWiiBox]

@dataclass
class MspBoxNames:
    """Represents data values for the MSP_BOXNAMES command."""
    names: tuple[str]

@dataclass
class MspCompGps:
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: int

    direction_to_home: int

    update: int

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

    mag_declination: int

    battery_scale: int

    battery_warn_1: int

    battery_warn_2: int

    battery_critical: int

@dataclass
class MspMotor:
    """Represents data values for the MSP_MOTOR command."""
    motor1: int
    motor2: int
    motor3: int
    motor4: int
    motor5: int
    motor6: int
    motor7: int
    motor8: int

@dataclass
class MspMotorPins:
    """Represents data values for the MSP_MOTOR_PINS command."""
    values: tuple[int]

@dataclass
class MspPid:
    """Represents data values for the MSP_PID command."""
    roll_p: int
    roll_i: int
    roll_d: int

    pitch_p: int
    pitch_i: int
    pitch_d: int

    yaw_p: int
    yaw_i: int
    yaw_d: int

    alt_p: int
    alt_i: int
    alt_d: int

    pos_p: int
    pos_i: int
    pos_d: int

    posr_p: int
    posr_i: int
    posr_d: int

    navr_p: int
    navr_i: int
    navr_d: int

    level_p: int
    level_i: int
    level_d: int

    mag_p: int
    mag_i: int
    mag_d: int

    vel_p: int
    vel_i: int
    vel_d: int

@dataclass
class MspPidNames:
    """Represents data values for the MSP_PIDNAMES command."""
    names: tuple[str]

@dataclass
class MspRawGps:
    """Represents data values for the MSP_RAW_GPS command."""
    fix: int

    satellites: int

    latitude: int

    longitude: int

    altitude: int

    speed: int

    ground_course: int

@dataclass
class MspRawImu:
    """Represents data values for the MSP_RAW_IMU command."""
    acc_x: float
    acc_y: float
    acc_z: float

    gyro_x: float
    gyro_y: float
    gyro_z: float

    mag_x: float
    mag_y: float
    mag_z: float

@dataclass
class MspRc:
    """Represents data values for the MSP_RC command."""
    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux1: int

    aux2: int

    aux3: int

    aux4: int

@dataclass
class MspRcTuning:
    """Represents data values for the MSP_RC_TUNING command."""
    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int

@dataclass
class MspServo:
    """Represents data values for the MSP_SERVO command."""
    values: tuple[int]

@dataclass
class MspServoConf:
    """Represents data values for the MSP_SERVO_CONF command."""
    values: tuple[int]

@dataclass
class MspStatus:
    """Represents data values for the MSP_STATUS command."""
    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int

@dataclass
class MspWaypoint:
    """Represents data values for the MSP_WP command."""
    number: int

    latitude: int

    longitude: int

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int

@dataclass
class BoxItem:
    """Represents  for the MSP_SET_BOX command."""
    aux1: MultiWiiBoxState
    aux2: MultiWiiBoxState
    aux3: MultiWiiBoxState
    aux4: MultiWiiBoxState
     
    def compile(self) -> int:
        """Compiles all of the set box state values to a single unsigned integer value."""
        pass

@dataclass
class Misc:
    """Represents data values for the MSP_SET_MISC command."""
    power_trigger: int

    throttle_min: int

    throttle_max: int

    min_command: int

    failsafe_throttle: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: int

    battery_scale: int

    battery_warn_1: int

    battery_warn_2: int

    battery_critical: int

@dataclass
class ServoConfItem:
    """Represents data values for the MSP_SET_SERVO_CONF command."""
    min: int

    max: int

    middle: int

    rate: int
