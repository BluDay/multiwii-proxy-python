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

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def ident(self) -> Ident:
        """Deserializes the retrieved MSP_IDENT message."""
        return self._deserialize(MspCommands.IDENT, Ident)

    @property
    def status(self) -> Status:
        """Deserializes the retrieved MSP_STATUS message."""
        return self._deserialize(MspCommands.STATUS, Status)

    @property
    def raw_imu(self) -> RawImu:
        """Deserializes the retrieved MSP_RAW_IMU message."""
        return self._deserialize(MspCommands.RAW_IMU, RawImu)

    @property
    def servo(self) -> Servo:
        """Deserializes the retrieved MSP_SERVO message."""
        return self._deserialize(MspCommands.SERVO, Servo)

    @property
    def servo_conf(self) -> ServoConf:
        """Deserializes the retrieved MSP_SERVO_CONF message."""
        return self._deserialize(MspCommands.SERVO_CONF, ServoConf)

    @property
    def motor(self) -> Motor:
        """Deserializes the retrieved MSP_MOTOR message."""
        return self._deserialize(MspCommands.MOTOR, Motor)

    @property
    def motor_pins(self) -> MotorPins:
        """Deserializes the retrieved MSP_MOTOR_PINS message."""
        return self._deserialize(MspCommands.MOTOR_PINS, MotorPins)

    @property
    def rc(self) -> Rc:
        """Deserializes the retrieved MSP_RC message."""
        return self._deserialize(MspCommands.RC, Rc)

    @property
    def rc_tuning(self) -> RcTuning:
        """Deserializes the retrieved MSP_RC_TUNING message."""
        return self._deserialize(MspCommands.RC_TUNING, RcTuning)
    
    @property
    def attitude(self) -> Attitude:
        """Deserializes the retrieved MSP_ATTITUDE message."""
        return self._deserialize(MspCommands.ATTITUDE, Attitude)

    @property
    def altitude(self) -> Altitude:
        """Deserializes the retrieved MSP_ALTITUDE message."""
        return self._deserialize(MspCommands.ALTITUDE, Altitude)

    @property
    def raw_gps(self) -> RawGps:
        """Deserializes the retrieved MSP_RAW_GPS message."""
        return self._deserialize(MspCommands.RAW_GPS, RawGps)

    @property
    def comp_gps(self) -> CompGps:
        """Deserializes the retrieved MSP_COMP_GPS message."""
        return self._deserialize(MspCommands.COMP_GPS, CompGps)

    @property
    def wp(self) -> Waypoint:
        """Deserializes the retrieved MSP_WP message."""
        return self._deserialize(MspCommands.WP, Waypoint)

    @property
    def analog(self) -> Analog:
        """Deserializes the retrieved MSP_ANALOG message."""
        return self._deserialize(MspCommands.ANALOG, Analog)

    @property
    def pid(self) -> Pid:
        """Deserializes the retrieved MSP_PID message."""
        return self._deserialize(MspCommands.PID, Pid)

    @property
    def pidnames(self) -> PidNames:
        """Deserializes the retrieved MSP_PIDNAMES message."""
        return self._deserialize(MspCommands.PIDNAMES, PidNames)

    @property
    def box(self) -> Box:
        """Deserializes the retrieved MSP_BOX message."""
        return self._deserialize(MspCommands.BOX, Box)

    @property
    def boxnames(self) -> BoxNames:
        """Deserializes the retrieved MSP_BOXNAMES message."""
        return self._deserialize(MspCommands.BOXNAMES, BoxNames)

    @property
    def boxids(self) -> BoxIds:
        """Deserializes the retrieved MSP_BOXIDS message."""
        return self._deserialize(MspCommands.BOXIDS, BoxIds)

    @property
    def misc(self) -> Misc:
        """Deserializes the retrieved MSP_MISC message."""
        return self._deserialize(MspCommands.MISC, Misc)
