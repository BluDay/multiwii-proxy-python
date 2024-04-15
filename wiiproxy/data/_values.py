from .altitude   import Altitude
from .analog     import Analog
from .attitude   import Attitude
from .box        import Box
from .box_ids    import BoxIds
from .box_names  import BoxNames
from .comp_gps   import CompGps
from .ident      import Ident
from .misc       import Misc
from .motor      import Motor
from .motor_pins import MotorPins
from .pid        import Pid
from .pid_names  import PidNames
from .raw_gps    import RawGps
from .raw_imu    import RawImu
from .rc         import Rc
from .rc_tuning  import RcTuning
from .servo      import Servo
from .servo_conf import ServoConf
from .status     import Status
from .waypoint   import Waypoint

class MultiWiiDataValues(object):
    """Represents a collection of data values for all MultiWii structures."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _ident:      Ident
    _status:     Status
    _raw_imu:    RawImu
    _servo:      Servo
    _servo_conf: ServoConf
    _motor:      Motor
    _motor_pins: MotorPins
    _rc:         Rc
    _rc_tuning:  RcTuning
    _attitude:   Attitude
    _altitude:   Altitude
    _raw_gps:    RawGps
    _comp_gps:   CompGps
    _waypoint:   Waypoint
    _analog:     Analog
    _pid:        Pid
    _pid_names:  PidNames
    _box:        Box
    _box_names:  BoxNames
    _box_ids:    BoxIds
    _misc:       Misc

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def ident(self) -> Ident:
        """Gets the data instance for MSP_IDENT."""
        return self._ident

    @property
    def status(self) -> Status:
        """Gets the data instance for MSP_STATUS."""
        return self._status

    @property
    def raw_imu(self) -> RawImu:
        """Gets the data instance for MSP_RAW_IMU."""
        return self._raw_imu

    @property
    def servo(self) -> Servo:
        """Gets the data instance for MSP_SERVO."""
        return self._servo

    @property
    def servo_conf(self) -> ServoConf:
        """Gets the data instance for MSP_SERVO_CONF."""
        return self._servo_conf

    @property
    def motor(self) -> Motor:
        """Gets the data instance for MSP_MOTOR."""
        return self._motor

    @property
    def motor_pins(self) -> MotorPins:
        """Gets the data instance for MSP_MOTOR_PINS."""
        return self._motor_pins

    @property
    def rc(self) -> Rc:
        """Gets the data instance for MSP_RC."""
        return self._rc

    @property
    def rc_tuning(self) -> RcTuning:
        """Gets the data instance for MSP_RC_TUNING."""
        return self._rc_tuning
    
    @property
    def attitude(self) -> Attitude:
        """Gets the data instance for MSP_ATTITUDE."""
        return self._attitude

    @property
    def altitude(self) -> Altitude:
        """Gets the data instance for MSP_ALTITUDE."""
        return self._altitude

    @property
    def raw_gps(self) -> RawGps:
        """Gets the data instance for MSP_RAW_GPS."""
        return self._raw_gps

    @property
    def comp_gps(self) -> CompGps:
        """Gets the data instance for MSP_COMP_GPS."""
        return self._comp_gps

    @property
    def waypoint(self) -> Waypoint:
        """Gets the data instance for MSP_WP."""
        return self._waypoint

    @property
    def analog(self) -> Analog:
        """Gets the data instance for MSP_ANALOG."""
        return self._analog

    @property
    def pid(self) -> Pid:
        """Gets the data instance for MSP_PID."""
        return self._pid

    @property
    def pidnames(self) -> PidNames:
        """Gets the data instance for MSP_PIDNAMES."""
        return self._pid_names

    @property
    def box(self) -> Box:
        """Gets the data instance for MSP_BOX."""
        return self._box

    @property
    def boxnames(self) -> BoxNames:
        """Gets the data instance for MSP_BOXNAMES."""
        return self._box_names

    @property
    def boxids(self) -> BoxIds:
        """Gets the data instance for MSP_BOXIDS."""
        return self._box_ids

    @property
    def misc(self) -> Misc:
        """Gets the data instance for MSP_MISC."""
        return self._misc
