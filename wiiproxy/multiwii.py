from . import (
    MSP_ALTITUDE,
    MSP_ANALOG,
    MSP_ATTITUDE,
    MSP_BOX,
    MSP_BOXIDS,
    MSP_BOXNAMES,
    MSP_COMP_GPS,
    MSP_IDENT,
    MSP_MISC,
    MSP_MOTOR,
    MSP_MOTOR_PINS,
    MSP_PID,
    MSP_PIDNAMES,
    MSP_RAW_GPS,
    MSP_RAW_IMU,
    MSP_RC,
    MSP_RC_TUNING,
    MSP_SERVO,
    MSP_SERVO_CONF,
    MSP_STATUS,
    MSP_WP,
    MSP_SET_RAW_RC,
    MSP_SET_RAW_GPS,
    MSP_SET_PID,
    MSP_SET_BOX,
    MSP_SET_RC_TUNING,
    MSP_ACC_CALIBRATION,
    MSP_MAG_CALIBRATION,
    MSP_SET_MISC,
    MSP_RESET_CONF,
    MSP_SET_HEAD,
    MSP_SET_SERVO_CONF,
    MSP_SET_MOTOR,
    MSP_BIND,
    MSP_EEPROM_WRITE
)

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

from serial import Serial
from time   import sleep
from typing import Final, NoReturn

class MultiWii(object):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial port—with a baudrate of 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default delay (in seconds) for serial writes."""
    DEFAULT_COMMAND_WRITE_DELAY: Final[float] = 0.005

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

    _command_write_delay: int

    _serial: Serial

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial port."""
        self._is_active = False

        if not isinstance(serial, Serial):
            raise TypeError('Argument "serial" must be an instance of "serial.Serial".')

        self._reset_data_values()

        self._serial = serial

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def altitude(self) -> Altitude:
        """Sends the MSP_ALTITUDE command and gets the data instance."""
        return self._altitude

    @property
    def analog(self) -> Analog:
        """Sends the MSP_ANALOG command and gets the data instance."""
        return self._analog

    @property
    def attitude(self) -> Attitude:
        """Sends the MSP_ATTITUDE command and gets the data instance."""
        return self._attitude
    
    @property
    def box(self) -> Box:
        """Sends the MSP_BOX command and gets the data instance."""
        return self._box

    @property
    def boxids(self) -> BoxIds:
        """Sends the MSP_BOXIDS command and gets the data instance."""
        return self._box_ids

    @property
    def boxnames(self) -> BoxNames:
        """Sends the MSP_BOXNAMES command and gets the data instance."""
        return self._box_names
    
    @property
    def comp_gps(self) -> CompGps:
        """Sends the MSP_COMP_GPS command and gets the data instance."""
        return self._comp_gps

    @property
    def ident(self) -> Ident:
        """Sends the MSP_IDENT command and gets the data instance."""
        return self._ident

    @property
    def misc(self) -> Misc:
        """Sends the MSP_MISC command and gets the data instance."""
        return self._misc

    @property
    def motor(self) -> Motor:
        """Sends the MSP_MOTOR command and gets the data instance."""
        return self._motor

    @property
    def motor_pins(self) -> MotorPins:
        """Sends the MSP_MOTOR_PINS command and gets the data instance."""
        return self._motor_pins
    
    @property
    def pid(self) -> Pid:
        """Sends the MSP_PID command and gets the data instance."""
        return self._pid

    @property
    def pidnames(self) -> PidNames:
        """Sends the MSP_PIDNAMES command and gets the data instance."""
        return self._pid_names

    @property
    def raw_gps(self) -> RawGps:
        """Sends the MSP_RAW_GPS command and gets the data instance."""
        return self._raw_gps

    @property
    def raw_imu(self) -> RawImu:
        """Sends the MSP_RAW_IMU command and gets the data instance."""
        return self._raw_imu

    @property
    def rc(self) -> Rc:
        """Sends the MSP_RC command and gets the data instance."""
        return self._rc

    @property
    def rc_tuning(self) -> RcTuning:
        """Sends the MSP_RC_TUNING command and gets the data instance."""
        return self._rc_tuning

    @property
    def servo(self) -> Servo:
        """Sends the MSP_SERVO command and gets the data instance."""
        return self._servo

    @property
    def servo_conf(self) -> ServoConf:
        """Sends the MSP_SERVO_CONF command and gets the data instance."""
        return self._servo_conf

    @property
    def status(self) -> Status:
        """Sends the MSP_STATUS command and gets the data instance."""
        return self._status

    @property
    def waypoint(self) -> Waypoint:
        """Sends the MSP_WP command and gets the data instance."""
        return self._waypoint

    @property
    def command_write_delay(self) -> float:
        """Gets the command write delay."""
        return self._command_write_delay

    @property
    def serial(self) -> Serial:
        """Gets the used serial instance that was provided at instantiation."""
        return self._serial

    @command_write_delay.setter
    def command_write_delay(self, value: float) -> NoReturn:
        """Sends the write delay value."""
        if not isinstance(value, float):
            raise TypeError('Value must be a float.')

        if value < 0:
            raise ValueError('Value must be a non-negative number.')
            
        self._command_write_delay = value

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

    def _reset_serial_buffers(self) -> NoReturn:
        """Resets the input and output buffers of the serial port.

        This method clears both the input and output buffers of the serial port,
        ensuring that any residual or incomplete data is discarded. It can be
        useful to call this method before initiaing new communication sessions
        or when the integrity of the data transfer needs to be ensured.

        Note
        ----
        This method directly accesses the underlying serial port object (_serial).
        Ensure that the serial port has been properly initialized before calling
        this method.

        Raises
        ------
        SerialException
            If an error occurs while resetting the buffers.
        """
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

    # ------------------------------------- SET COMMANDS ---------------------------------------

    def bind_transmitter_receiver(self) -> NoReturn:
        """Sends the MSP_BIND command.

        This command initiates the binding process between the transmitter (radio controller)
        and the receiver connected to the FC. Binding establishes a secure communication link
        between the transmitter (TX) and the receiver (RX).

        Note
        ----
        Ensure that the FC is ready to receive the bind command and that the transmitter is in
        binding mode before calling this method.
        """
        self._send_message(MSP_BIND)

    def calibrate_accelerometer(self) -> NoReturn:
        """Sends the MSP_ACC_CALIBRATION command.

        This command initiates the accelerometer calibration process on the FC. Accelerometer
        calibration is essential for accurate attitude estimation and stabilization of the
        aircraft.

        Note
        ----
        The FC should be placed on a level surface during the calibration to ensure accurate
        results. Avoid moving or disturbing the FC during the process.
        """
        self._send_message(MSP_ACC_CALIBRATION)

    def calibrate_magnetometer(self) -> NoReturn:
        """Sends the MSP_MAG_CALIBRATION command.

        This command initiates the magnetometer (compass) calibration process on the FC.
        Magnetometer calibration is crucial for accurate heading estimation and navigation,
        especially in GPS-assisted flight modes.

        Note
        ----
        The FC should be rotated along all three axes (roll, pitch, yaw) in a smooth and
        consistent manner to ensure accurate results. Avoid any magnetic interference or
        disturbances during the process.
        """
        self._send_message(MSP_ACC_CALIBRATION)

    def reset_config(self) -> NoReturn:
        """Sends the MSP_RESET_CONF command.

        This command resets the configuration settings on the FC to their default values.
        It effectively restores the FC to its initial configuration state, clearing any
        customized settings or adjustments made by the user.

        Note
        ----
        Resetting the config should be done with caution, as it will revert all settings to
        their defaults. Make sure to reconfigure the FC according to your requirements after
        executing this command.
        """
        self._send_message(MSP_RESET_CONF)

    def save_config_to_eeprom(self) -> NoReturn:
        """Sends the MSP_EEPROM_WRITE command.

        This command writes the current configuration settings to the EEPROM of the FC. 

        Note
        ----
        Writing to EEPROM should be done with caution, as it modifies the stored config
        directly. Ensure that the values written are valid and intended, as incorrect
        values could lead to unexpected behavior or instability.
        """
        self._send_message(MSP_EEPROM_WRITE)

    def set_box(self) -> NoReturn:
        """Sends the MSP_SET_BOX

        Sets the flight modes (or "boxes") config on the FC. Flight modes define the behavior
        of the aircraft based on various inputs from the transmitter or other sources.
        """
        self._send_message(MSP_SET_BOX)

    def set_head(self) -> NoReturn:
        """Sends the MSP_SET_HEAD command.

        Sets the heading (yaw) direction reference on the FC. It is used to define the forward
        direction of the aircraft relative to its orientation.
        """
        self._send_message(MSP_SET_HEAD)

    def set_misc(self) -> NoReturn:
        """Sends the MSP_SET_MISC command.

        Sets miscellaneous config parameters on the FC—such as battery voltage scaling, failsafe
        behavior, or other settings not covered by specific MSP commands.
        """
        self._send_message(MSP_SET_MISC)

    def set_motor(self) -> NoReturn:
        """Sends the MSP_SET_MOTOR command.

        Sets the motor output values on the FC. Motor output values determine the throttle level
        for each motor, controlling the rotation speed and thrust generated by the motors.
        """
        self._send_message(MSP_SET_MOTOR)

    def set_pid(self) -> NoReturn:
        """Sends the MSP_SET_PID command.

        Sets the PID values on the FC. PID values are used to adjust the stability and response
        characteristics of the aircraft.
        """
        self._send_message(MSP_SET_PID)

    def set_raw_gps(self) -> NoReturn:
        """Sends the MSP_SET_RAW_GPS command.

        Sets the raw GPS data on the FC—such as the latitude, longitude, altitude, and other
        GPS-related information.
        """
        self._send_message(MSP_SET_RAW_GPS)

    def set_raw_rc(self) -> NoReturn:
        """Sends the MSP_SET_RAW_RC command.

        Sets the raw receiver (RC/RX) channel data on the FC. Raw FC data includes the pulse
        width values received from the transmitter for each channel, typically representing
        control inputs such as throttle, pitch, roll, and yaw.
        """
        self._send_message(MSP_SET_RAW_RC)
    
    def set_rc_tuning(self) -> NoReturn:
        """Sends the MSP_SET_RC_TUNING command.

        Sets RC tuning parameters on the FC—such as expo, rates, and other settings related to
        RC control response and behavior.
        """
        self._send_message(MSP_SET_RC_TUNING)

    def set_servo_conf(self) -> NoReturn:
        """Sends the MSP_SET_SERVO_CONF command.

        Sets servo config parameters on the FC—such as servo mapping, direction, endpoints, and
        other settings related to servo control.
        """
        self._send_message(MSP_SET_SERVO_CONF)
