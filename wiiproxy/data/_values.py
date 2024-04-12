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

from dataclasses import dataclass
from typing      import NoReturn

@dataclass(slots=True)
class _MultiWiiDataValues(object):
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
