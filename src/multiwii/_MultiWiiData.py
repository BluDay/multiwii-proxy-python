from .data import *

"""
Saved commands from the instance for MSP_evious codebase:

    {NAME} = ({CODE}, {STRUCT_FORMAT}, {HAS_VARIABLE_DATA_SIZE}, {PRIORITY_TYPE})

    # Get commands.
	MSP_IDENT      = (100, '3BI',    0, Inactive)
	MSP_STATUS     = (101, '3HIB',   0, Inactive)
	MSP_RAW_IMU    = (102, '9h',     0, High)
	MSP_SERVO      = (103, '8H',     0, Normal)
	MSP_MOTOR      = (104, '8H',     0, High)
	MSP_RC         = (105, '8H',     0, Critical)
	MSP_RAW_GPS    = (106, '2B2I3H', 0, Inactive)
	MSP_COMP_GPS   = (107, '2HB',    0, Inactive)
	MSP_ATTITUDE   = (108, '3h',     0, High)
	MSP_ALTITUDE   = (109, 'ih',     0, High)
	MSP_ANALOG     = (110, 'B3H',    0, Inactive)
	MSP_RC_TUNING  = (111, '7B',     0, Inactive)
	MSP_PID        = (112, '30B',    0, Inactive)
	MSP_BOX        = (113, 'H',      1, Inactive)
	MSP_MISC       = (114, '6HIH4B', 0, Inactive)
	MSP_MOTOR_PINS = (115, '8B',     0, Inactive)
	MSP_BOXNAMES   = (116, 's',      1, Inactive)
	MSP_PIDNAMES   = (117, 's',      1, Inactive)
	MSP_WP         = (118, 'B3I2HB', 0, Inactive)
	MSP_BOXIDS     = (119, 'B',      1, Inactive)
	MSP_SERVO_CONF = (120, '3HB',    1, Inactive)

    # Set commands.
	MSP_SET_RAW_RC      = (200, '8H',     0, Critical)
	MSP_SET_RAW_GPS     = (201, '2B2I2H', 0, Inactive)
	MSP_SET_PID         = (202, '30B',    0, Inactive)
	MSP_SET_BOX         = (203, 'H',      1, Inactive)
	MSP_SET_RC_TUNING   = (204, '7B',     0, Inactive)
	MSP_ACC_CALIBRATION = (205, '',       0, Inactive)
	MSP_MAG_CALIBRATION = (206, '',       0, Inactive)
	MSP_SET_MISC        = (207, '6HIH4B', 0, Inactive)
	MSP_RESET_CONF      = (208, '',       0, Inactive)
	MSP_SET_HEAD        = (211, 'h',      0, Inactive)
	MSP_SET_SERVO_CONF  = (212, '56B',    0, Inactive)
	MSP_SET_MOTOR       = (214, '8H',     0, Inactive)
	MSP_BIND            = (240, '',       0, Inactive)
	MSP_EEPROM_WRITE    = (250, '',       0, Inactive)
"""

class _MultiWiiData(object):
    """
    The mixin class used for initializing all MultiWii data value instances and creating
    corresponding private fields for an instance of this type, or of a derived type.
    """
    
    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def ident(self) -> Ident:
        """
        Gets the instance for MSP_IDENT.
        """
        return self._ident

    @property
    def status(self) -> Status:
        """
        Gets the instance for MSP_STATUS.
        """
        return self._status

    @property
    def raw_imu(self) -> RawImu:
        """
        Gets the instance for MSP_RAW_IMU.
        """
        return self._raw_imu

    @property
    def servo(self) -> Servo:
        """
        Gets the instance for MSP_SERVO.
        """
        return self._servo

    @property
    def servo_conf(self) -> ServoConf:
        """
        Gets the instance for MSP_SERVO_CONF.
        """
        return self._servo_conf

    @property
    def motor(self) -> Motor:
        """
        Gets the instance for MSP_MOTOR.
        """
        return self._motor

    @property
    def motor_pins(self) -> MotorPins:
        """
        Gets the instance for MSP_MOTOR_PINS.
        """
        return self._motor_pins

    @property
    def rc(self) -> Rc:
        """
        Gets the instance for MSP_RC.
        """
        return self._rc

    @property
    def rc_tuning(self) -> RcTuning:
        """
        Gets the instance for MSP_RC_TUNING.
        """
        return self._rc_tuning

    @property
    def attitude(self) -> Attitude:
        """
        Gets the instance for MSP_ATTITUDE.
        """
        return self._attitude

    @property
    def altitude(self) -> Altitude:
        """
        Gets the instance for MSP_ALTITUDE.
        """
        return self._altitude

    @property
    def raw_gps(self) -> RawGps:
        """
        Gets the instance for MSP_RAW_GPS.
        """
        return self._raw_gps

    @property
    def comp_gps(self) -> CompGps:
        """
        Gets the instance for MSP_COMP_GPS.
        """
        return self._comp_gps

    @property
    def waypoint(self) -> Waypoint:
        """
        Gets the instance for MSP_WP.
        """
        return self._waypoint

    @property
    def analog(self) -> Analog:
        """
        Gets the instance for MSP_AMALOG.
        """
        return self._analog

    @property
    def pid(self) -> Pid:
        """
        Gets the instance for MSP_PID.
        """
        return self._pid

    @property
    def pidnames(self) -> PidNames:
        """
        Gets the instance for MSP_PIDNAMES.
        """
        return self._pidnames

    @property
    def box(self) -> Box:
        """
        Gets the instance for MSP_BOX.
        """
        return self._box

    @property
    def boxnames(self) -> BoxNames:
        """
        Gets the instance for MSP_BOXNAMES.
        """
        return self._boxnames

    @property
    def boxids(self) -> BoxIds:
        """
        Gets the instance for MSP_BOXIDS.
        """
        return self._boxids

    @property
    def misc(self) -> Misc:
        """
        Gets the instance for MSP_MISC.
        """
        return self._misc

    # ------------------------------------ INSTANCE METHODS ------------------------------------

    def reset_data(self) -> None:
        """
        Resets all data value instances. defines each field if not already defined.
        """
        self._ident      = Ident()
        self._status     = Status()
        self._raw_imu    = RawImu()
        self._servo      = Servo()
        self._servo_conf = ServoConf()
        self._motor      = Motor()
        self._motor_pins = MotorPins()
        self._rc         = Rc()
        self._rc_tuning  = RcTuning()
        self._attitude   = Attitude()
        self._altitude   = Altitude()
        self._raw_gps    = RawGps()
        self._comp_gps   = CompGps()
        self._waypoint   = Waypoint()
        self._analog     = Analog()
        self._pid        = Pid()
        self._pidnames   = PidNames()
        self._box        = Box()
        self._boxnames   = BoxNames()
        self._boxids     = BoxIds()
        self._misc       = Misc()
