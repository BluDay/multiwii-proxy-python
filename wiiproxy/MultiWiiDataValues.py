from .data import (
    Altitude,
    Analog,
    Attitude,
    Box,
    BoxIds,
    BoxNames,
    CompGps,
    Ident,
    Misc,
    Motor,
    MotorPins,
    Pid,
    PidNames,
    RawGps,
    RawImu,
    Rc,
    RcTuning,
    Servo,
    ServoConf,
    Status,
    Waypoint
)

from dataclasses import dataclass

@dataclass(slots=True)
class MultiWiiDataValues(object):
    """
    The class used for initializing all MSP data value instances and creating
    corresponding private fields for an instance of this type, or of a derived type.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

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

    def reset_data(self) -> None:
        """
        Resets all data value instances. defines each field if not already defined.
        """
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
