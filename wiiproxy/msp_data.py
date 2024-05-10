from .data import (
    MspAltitude,
    MspAnalog,
    MspAttitude,
    MspBox,
    MspBoxIds,
    MspBoxNames,
    MspCompGps,
    MspIdent,
    MspMisc,
    MspMotor,
    MspMotorPins,
    MspPid,
    MspPidNames,
    MspRawGps,
    MspRawImu,
    MspRc,
    MspRcTuning,
    MspServo,
    MspServoConf,
    MspStatus,
    MspWaypoint
)

from typing import Final, NoReturn

class MspData(object):
    """A collection of all MSP data structure instances."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _altitude:   MspAltitude
    _analog:     MspAnalog
    _attitude:   MspAttitude
    _box:        MspBox
    _box_ids:    MspBoxIds
    _box_names:  MspBoxNames
    _comp_gps:   MspCompGps
    _ident:      MspIdent
    _misc:       MspMisc
    _motor:      MspMotor
    _motor_pins: MspMotorPins
    _pid:        MspPid
    _pid_names:  MspPidNames
    _raw_gps:    MspRawGps
    _raw_imu:    MspRawImu
    _rc:         MspRc
    _rc_tuning:  MspRcTuning
    _servo:      MspServo
    _servo_conf: MspServoConf
    _status:     MspStatus
    _waypoint:   MspWaypoint

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def altitude(self) -> MspAltitude:
        """Sends the MSP_ALTITUDE command and gets the data instance."""
        return self._altitude
    
    @property
    def analog(self) -> MspAnalog:
        """Sends the MSP_ANALOG command and gets the data instance."""
        return self._analog
    
    @property
    def attitude(self) -> MspAttitude:
        """Sends the MSP_ATTITUDE command and gets the data instance."""
        return self._attitude
    
    @property
    def box(self) -> MspBox:
        """Sends the MSP_BOX command and gets the data instance."""
        return self._box
    
    @property
    def box_ids(self) -> MspBoxIds:
        """Sends the MSP_BOXIDS command and gets the data instance."""
        return self._boxids
    
    @property
    def box_names(self) -> MspBoxNames:
        """Sends the MSP_BOXNAMES command and gets the data instance."""
        return self._boxnames
    
    @property
    def comp_gps(self) -> MspCompGps:
        """Sends the MSP_COMP_GPS command and gets the data instance."""
        return self._comp_gps
    
    @property
    def ident(self) -> MspIdent:
        """Sends the MSP_IDENT command and gets the data instance."""
        return self._ident
    
    @property
    def misc(self) -> MspMisc:
        """Sends the MSP_MISC command and gets the data instance."""
        return self._misc
    
    @property
    def motor(self) -> MspMotor:
        """Sends the MSP_MOTOR command and gets the data instance."""
        return self._motor
    
    @property
    def motor_pins(self) -> MspMotorPins:
        """Sends the MSP_MOTOR_PINS command and gets the data instance."""
        return self._motor_pins
    
    @property
    def pid(self) -> MspPid:
        """Sends the MSP_PID command and gets the data instance."""
        return self._pid
    
    @property
    def pid_names(self) -> MspPidNames:
        """Sends the MSP_PIDNAMES command and gets the data instance."""
        return self._pid_names
    
    @property
    def raw_gps(self) -> MspRawGps:
        """Sends the MSP_RAW_GPS command and gets the data instance."""
        return self._raw_gps
    
    @property
    def raw_imu(self) -> MspRawImu:
        """Sends the MSP_RAW_IMU command and gets the data instance."""
        return self._raw_imu
    
    @property
    def rc(self) -> MspRc:
        """Sends the MSP_RC command and gets the data instance."""
        return self._rc
    
    @property
    def rc_tuning(self) -> MspRcTuning:
        """Sends the MSP_RC_TUNING command and gets the data instance."""
        return self._rc_tuning
    
    @property
    def servo(self) -> MspServo:
        """Sends the MSP_SERVO command and gets the data instance."""
        return self._servo
    
    @property
    def servo_conf(self) -> MspServoConf:
        """Sends the MSP_SERVO_CONF command and gets the data instance."""
        return self._servo_conf
    
    @property
    def status(self) -> MspStatus:
        """Sends the MSP_STATUS command and gets the data instance."""
        return self._status
    
    @property
    def waypoint(self) -> MspWaypoint:
        """Sends the MSP_WP command and gets the data instance."""
        return self._waypoint

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _reset(self) -> NoReturn:
        """Resets all data value instances."""
        self._altitude   = MspAltitude()
        self._analog     = MspAnalog()
        self._attitude   = MspAttitude()
        self._box        = MspBox()
        self._box_ids    = MspBoxIds()
        self._box_names  = MspBoxNames()
        self._comp_gps   = MspCompGps()
        self._ident      = MspIdent()
        self._misc       = MspMisc()
        self._motor      = MspMotor()
        self._motor_pins = MspMotorPins()
        self._pid        = MspPid()
        self._pid_names  = MspPidNames()
        self._raw_gps    = MspRawGps()
        self._raw_imu    = MspRawImu()
        self._rc         = MspRc()
        self._rc_tuning  = MspRcTuning()
        self._servo      = MspServo()
        self._servo_conf = MspServoConf()
        self._status     = MspStatus()
        self._waypoint   = MspWaypoint()
