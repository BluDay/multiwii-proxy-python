from .data import (
    Altitude
    Analog
    Attitude
    Box
    BoxIds
    BoxNames
    CompGps
    Ident
    Misc
    Motor
    MotorPins
    Pid
    PidNames
    RawGps
    RawImu
    Rc
    RcTuning
    Servo
    ServoConf
    Status
    Waypoint
)

from dataclasses import dataclass

"""
Saved commands from the instance for MSP_evious codebase

    {NAME} = ({CODE}, {STRUCT_FORMAT}, {HAS_VARIABLE_DATA_SIZE}, {PRIORITY_TYPE})

    # Get commands.
    MSP_IDENT      = (100, '3BI',    False, Inactive)
    MSP_STATUS     = (101, '3HIB',   False, Inactive)
    MSP_RAW_IMU    = (102, '9h',     False, High)
    MSP_SERVO      = (103, '8H',     False, Normal)
    MSP_MOTOR      = (104, '8H',     False, High)
    MSP_RC         = (105, '8H',     False, Critical)
    MSP_RAW_GPS    = (106, '2B2I3H', False, Inactive)
    MSP_COMP_GPS   = (107, '2HB',    False, Inactive)
    MSP_ATTITUDE   = (108, '3h',     False, High)
    MSP_ALTITUDE   = (109, 'ih',     False, High)
    MSP_ANALOG     = (110, 'B3H',    False, Inactive)
    MSP_RC_TUNING  = (111, '7B',     False, Inactive)
    MSP_PID        = (112, '30B',    False, Inactive)
    MSP_BOX        = (113, 'H',      True,  Inactive)
    MSP_MISC       = (114, '6HIH4B', False, Inactive)
    MSP_MOTOR_PINS = (115, '8B',     False, Inactive)
    MSP_BOXNAMES   = (116, 's',      True,  Inactive)
    MSP_PIDNAMES   = (117, 's',      True,  Inactive)
    MSP_WP         = (118, 'B3I2HB', False, Inactive)
    MSP_BOXIDS     = (119, 'B',      True,  Inactive)
    MSP_SERVO_CONF = (120, '3HB',    True,  Inactive)

    # Set commands.
    MSP_SET_RAW_RC      = (200, '8H',     False, Critical)
    MSP_SET_RAW_GPS     = (201, '2B2I2H', False, Inactive)
    MSP_SET_PID         = (202, '30B',    False, Inactive)
    MSP_SET_BOX         = (203, 'H',      True,  Inactive)
    MSP_SET_RC_TUNING   = (204, '7B',     False, Inactive)
    MSP_ACC_CALIBRATION = (205, '',       False, Inactive)
    MSP_MAG_CALIBRATION = (206, '',       False, Inactive)
    MSP_SET_MISC        = (207, '6HIH4B', False, Inactive)
    MSP_RESET_CONF      = (208, '',       False, Inactive)
    MSP_SET_HEAD        = (211, 'h',      False, Inactive)
    MSP_SET_SERVO_CONF  = (212, '56B',    False, Inactive)
    MSP_SET_MOTOR       = (214, '8H',     False, Inactive)
    MSP_BIND            = (240, '',       False, Inactive)
    MSP_EEPROM_WRITE    = (250, '',       False, Inactive)
"""

@dataclass(slots=True)
class _MultiWiiDataValues(object)
    """
    The class used for initializing all MultiWii data value instances and creating
    corresponding private fields for an instance of this type, or of a derived type.
    """
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
