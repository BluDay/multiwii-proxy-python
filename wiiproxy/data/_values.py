from ._base import MultiWiiDataStructure

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
    _wp:         Waypoint
    _analog:     Analog
    _pid:        Pid
    _pidnames:   PidNames
    _box:        Box
    _boxnames:   BoxNames
    _boxids:     BoxIds
    _misc:       Misc

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def ident(self) -> Ident:
        """Deserializes the retrieved MSP_IDENT message."""
        return self._ident

    @property
    def status(self) -> Status:
        """Deserializes the retrieved MSP_STATUS message."""
        return self._status

    @property
    def raw_imu(self) -> RawImu:
        """Deserializes the retrieved MSP_RAW_IMU message."""
        return self._raw_imu

    @property
    def servo(self) -> Servo:
        """Deserializes the retrieved MSP_SERVO message."""
        return self._servo

    @property
    def servo_conf(self) -> ServoConf:
        """Deserializes the retrieved MSP_SERVO_CONF message."""
        return self._servo_conf

    @property
    def motor(self) -> Motor:
        """Deserializes the retrieved MSP_MOTOR message."""
        return self._motor

    @property
    def motor_pins(self) -> MotorPins:
        """Deserializes the retrieved MSP_MOTOR_PINS message."""
        return self._motor_pins

    @property
    def rc(self) -> Rc:
        """Deserializes the retrieved MSP_RC message."""
        return self._rc

    @property
    def rc_tuning(self) -> RcTuning:
        """Deserializes the retrieved MSP_RC_TUNING message."""
        return self._rc_tuning
    
    @property
    def attitude(self) -> Attitude:
        """Deserializes the retrieved MSP_ATTITUDE message."""
        return self._attitude

    @property
    def altitude(self) -> Altitude:
        """Deserializes the retrieved MSP_ALTITUDE message."""
        return self._altitude

    @property
    def raw_gps(self) -> RawGps:
        """Deserializes the retrieved MSP_RAW_GPS message."""
        return self._raw_gps

    @property
    def comp_gps(self) -> CompGps:
        """Deserializes the retrieved MSP_COMP_GPS message."""
        return self._comp_gps

    @property
    def wp(self) -> Waypoint:
        """Deserializes the retrieved MSP_WP message."""
        return self._wp

    @property
    def analog(self) -> Analog:
        """Deserializes the retrieved MSP_ANALOG message."""
        return self._analog

    @property
    def pid(self) -> Pid:
        """Deserializes the retrieved MSP_PID message."""
        return self._pid

    @property
    def pidnames(self) -> PidNames:
        """Deserializes the retrieved MSP_PIDNAMES message."""
        return self._pidnames

    @property
    def box(self) -> Box:
        """Deserializes the retrieved MSP_BOX message."""
        return self._box

    @property
    def boxnames(self) -> BoxNames:
        """Deserializes the retrieved MSP_BOXNAMES message."""
        return self._boxnames

    @property
    def boxids(self) -> BoxIds:
        """Deserializes the retrieved MSP_BOXIDS message."""
        return self._boxids

    @property
    def misc(self) -> Misc:
        """Deserializes the retrieved MSP_MISC message."""
        return self._misc
