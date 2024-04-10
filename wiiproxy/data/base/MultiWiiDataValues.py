from .. import (
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

from typing import NoReturn

class MultiWiiDataValues(object):
    """The class used for initializing all MSP data value instances.

    And for creating corresponding private fields for an instance of this type,
    or of a derived type.
    """

    # ------------------------------------ INSTANCE METHODS ------------------------------------

    def _reset_data(self) -> NoReturn:
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
