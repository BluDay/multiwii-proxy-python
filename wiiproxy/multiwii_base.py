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

from typing import Final, NoReturn

class MultiWiiBase(object):
    """Represents a collection of data values for all MultiWii structures."""

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """The MSP version used."""
    MSP_VERSION: Final[str] = 'v1'
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _altitude:   Altitude
    _analog:     Analog
    _attitude:   Attitude
    _box:        Box
    _box_ids:    BoxIds
    _box_names:  BoxNames
    _comp_gps:   CompGps
    _ident:      Ident
    _misc:       Misc
    _motor:      Motor
    _motor_pins: MotorPins
    _pid:        Pid
    _pid_names:  PidNames
    _raw_gps:    RawGps
    _raw_imu:    RawImu
    _rc:         Rc
    _rc_tuning:  RcTuning
    _servo:      Servo
    _servo_conf: ServoConf
    _status:     Status
    _waypoint:   Waypoint

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def altitude(self) -> Altitude:
        """Gets the data instance for MSP_ALTITUDE."""
        return self._altitude

    @property
    def analog(self) -> Analog:
        """Gets the data instance for MSP_ANALOG."""
        return self._analog

    @property
    def attitude(self) -> Attitude:
        """Gets the data instance for MSP_ATTITUDE."""
        return self._attitude
    
    @property
    def box(self) -> Box:
        """Gets the data instance for MSP_BOX."""
        return self._box

    @property
    def boxids(self) -> BoxIds:
        """Gets the data instance for MSP_BOXIDS."""
        return self._box_ids

    @property
    def boxnames(self) -> BoxNames:
        """Gets the data instance for MSP_BOXNAMES."""
        return self._box_names
    
    @property
    def comp_gps(self) -> CompGps:
        """Gets the data instance for MSP_COMP_GPS."""
        return self._comp_gps

    @property
    def ident(self) -> Ident:
        """Gets the data instance for MSP_IDENT."""
        return self._ident

    @property
    def misc(self) -> Misc:
        """Gets the data instance for MSP_MISC."""
        return self._misc

    @property
    def motor(self) -> Motor:
        """Gets the data instance for MSP_MOTOR."""
        return self._motor

    @property
    def motor_pins(self) -> MotorPins:
        """Gets the data instance for MSP_MOTOR_PINS."""
        return self._motor_pins
    
    @property
    def pid(self) -> Pid:
        """Gets the data instance for MSP_PID."""
        return self._pid

    @property
    def pidnames(self) -> PidNames:
        """Gets the data instance for MSP_PIDNAMES."""
        return self._pid_names

    @property
    def raw_gps(self) -> RawGps:
        """Gets the data instance for MSP_RAW_GPS."""
        return self._raw_gps

    @property
    def raw_imu(self) -> RawImu:
        """Gets the data instance for MSP_RAW_IMU."""
        return self._raw_imu

    @property
    def rc(self) -> Rc:
        """Gets the data instance for MSP_RC."""
        return self._rc

    @property
    def rc_tuning(self) -> RcTuning:
        """Gets the data instance for MSP_RC_TUNING."""
        return self._rc_tuning

    @property
    def servo(self) -> Servo:
        """Gets the data instance for MSP_SERVO."""
        return self._servo

    @property
    def servo_conf(self) -> ServoConf:
        """Gets the data instance for MSP_SERVO_CONF."""
        return self._servo_conf

    @property
    def status(self) -> Status:
        """Gets the data instance for MSP_STATUS."""
        return self._status

    @property
    def waypoint(self) -> Waypoint:
        """Gets the data instance for MSP_WP."""
        return self._waypoint

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _reset_data_values(self) -> NoReturn:
        """Resets all data values."""
        self._altitude   = Altitude()
        self._analog     = Analog()
        self._attitude   = Attitude()
        self._box        = Box()
        self._box_ids    = BoxIds()
        self._box_names  = BoxNames()
        self._comp_gps   = CompGps()
        self._ident      = Ident()
        self._misc       = Misc()
        self._motor      = Motor()
        self._motor_pins = MotorPins()
        self._pid        = Pid()
        self._pid_names  = PidNames()
        self._raw_gps    = RawGps()
        self._raw_imu    = RawImu()
        self._rc         = Rc()
        self._rc_tuning  = RcTuning()
        self._servo      = Servo()
        self._servo_conf = ServoConf()
        self._status     = Status()
        self._waypoint   = Waypoint()
