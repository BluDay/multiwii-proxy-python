from .command import Command

from .commands import (
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
    MSP_ACC_CALIBRATION,
    MSP_BIND,
    MSP_EEPROM_WRITE,
    MSP_MAG_CALIBRATION,
    MSP_RESET_CONF,
    MSP_SET_BOX,
    MSP_SET_HEAD,
    MSP_SET_MISC,
    MSP_SET_MOTOR,
    MSP_SET_PID,
    MSP_SET_RAW_RC,
    MSP_SET_RAW_GPS,
    MSP_SET_RC_TUNING,
    MSP_SET_SERVO_CONF
)

from .data import (
    MspAltitude,
    MspAnalog,
    MspAttitude,
    MspBox,
    MspBoxIds,
    MspBoxItem,
    MspBoxNames,
    MspCompGps,
    MspIdent,
    MspMisc,
    MspSetMisc,
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
    MspServoConfItem,
    MspStatus,
    MspWaypoint
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
    
    # -------------------------------------- CONSTANTS -----------------------------------------

    DEFAULT_MESSAGE_WRITE_READ_DELAY: Final[float] = 0.005

    MSP_VERSION: Final[int] = 1

    # -------------------------------------- ATTRIBUTES ----------------------------------------

    _message_write_read_delay: float

    _serial: Final[Serial]

    # ------------------------------------ DUNDER METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial port.

        This constructor initializes a new instance of the MultiWii class using the provided
        serial port for communication with the FC. It sets up the initial state of the object,
        including the activation status, command write-read delay and serial port configuration.
        Additionally, it ensures that the provided serial port is of the correct type (Serial).
        If the serial port is not of the expected type, a TypeError is raised.

        Parameters
        ----------
        serial : Serial
            The serial port instance used for communication with the flight controller. This
            should be an instance of the `Serial` class from the `pyserial` library, which
            provides the interface for serial communication.

        Raises
        ------
        TypeError
            If the provided serial port instance is not an instance of the `Serial` class.
        """
        if not isinstance(serial, Serial):
            raise TypeError('"serial" must be an instance of "Serial".')

        self._message_write_read_delay = self.DEFAULT_MESSAGE_WRITE_READ_DELAY

        self._serial = serial

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def message_write_read_delay(self) -> float:
        """Gets the delay (in seconds) between each write and read message."""
        return self._message_write_read_delay

    @property
    def serial(self) -> Serial:
        """Gets the used serial instance that was provided at instantiation."""
        return self._serial

    @message_write_read_delay.setter
    def message_write_read_delay(self, value: float) -> NoReturn:
        """Sets the delay (in seconds) between each write and read command.

        This property controls the delay between each write message followed by a read message
        sent to the FC. A message with empty data values is sent first, followed by a delay,
        and then a read message to retrieve information from the FC.

        Raises
        ------
        TypeError
            If the value is not a float.
        ValueError
            If the value is a negative number.
        """
        if not isinstance(value, float):
            raise TypeError('Value must be a float.')

        if value < 0:
            raise ValueError('Value must be a non-negative number.')
            
        self._message_write_read_delay = value

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _clear_serial_io_buffers(self) -> NoReturn:
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

    def _read_data(self, command: Command) -> tuple[int]:
        """Reads a message of the specified command and returns the unserialized data.

        Parameters
        ----------
        command : Command
            The MSP command to read a message for.

        Returns
        -------
        tuple[int]
            A tuple with the unserialized data values.
        """
        return self._read_message(command)[5:-1]

    def _read_message(self, command: Command) -> bytes:
        """Reads a message from the FC with the specified command code.

        Note
        ----
        This method sends a write message with empty values to the FC in order to retrieve a
        response message. Ensure that the FC is ready to to respond to the command code sent.

        Parameters
        ----------
        command : Command
            The MSP command to read a message for.

        Raises
        ------
        ValueError
            If the provided command code is invalid or not recognized.
        TimeoutError
            If a timeout occurs while waiting for the message from the FC.

        Returns
        -------
        bytes
            The bytes for the read/incoming message.
        """
        pass

    def _send_message(self, command: Command, data: tuple[int] = None) -> NoReturn:
        """Sends a message to the FC with the specified command code and optional data values.

        Parameters
        ----------
        command : Command
            The MSP command to create a message for.
        data : tuple[int]
            Data values to serialize and include in the message payload.

        Raises
        ------
        ValueError
            If the provided command code is invalid or not recognized.
        TimeoutError
            If a timeout occurs while waiting for the FC to acknowledge the message.
        """
        pass

    # --------------------------------- GET COMMAND METHODS ------------------------------------

    def get_altitude(self) -> MspAltitude:
        """Sends an MSP_ALTITUDE command and gets the data instance."""
        return MspAltitude.parse(self._read_data(MSP_ALTITUDE))
    
    def get_analog(self) -> MspAnalog:
        """Sends an MSP_ANALOG command and gets the data instance."""
        return MspAnalog.parse(self._read_data(MSP_ANALOG))
    
    def get_attitude(self) -> MspAttitude:
        """Sends an MSP_ATTITUDE command and gets the data instance."""
        return MspAttitude.parse(self._read_data(MSP_ATTITUDE))
    
    def get_box(self) -> MspBox:
        """Sends an MSP_BOX command and gets the data instance."""
        return MspBox.parse(self._read_data(MSP_BOX))
    
    def get_box_ids(self) -> MspBoxIds:
        """Sends an MSP_BOXIDS command and gets the data instance."""
        return MspBoxIds.parse(self._read_data(MSP_BOXIDS))
    
    def get_box_names(self) -> MspBoxNames:
        """Sends an MSP_BOXNAMES command and gets the data instance."""
        return MspBoxNames.parse(self._read_data(MSP_BOXNAMES))
    
    def get_comp_gps(self) -> MspCompGps:
        """Sends an MSP_COMP_GPS command and gets the data instance."""
        return MspCompGps.parse(self._read_data(MSP_COMP_GPS))
    
    def get_ident(self) -> MspIdent:
        """Sends an MSP_IDENT command and gets the data instance."""
        return MspIdent.parse(self._read_data(MSP_IDENT))
    
    def get_misc(self) -> MspMisc:
        """Sends an MSP_MISC command and gets the data instance."""
        return MspMisc.parse(self._read_data(MSP_MISC))
    
    def get_motor(self) -> MspMotor:
        """Sends an MSP_MOTOR command and gets the data instance."""
        return MspMotor.parse(self._read_data(MSP_MOTOR))
    
    def get_motor_pins(self) -> MspMotorPins:
        """Sends an MSP_MOTOR_PINS command and gets the data instance."""
        return MspMotorPins.parse(self._read_data(MSP_MOTOR_PINS))

    def get_pid(self) -> MspPid:
        """Sends an MSP_PID command and gets the data instance."""
        return MspPid.parse(self._read_data(MSP_PID))

    def get_pid_names(self) -> tuple[str]:
        """Sends an MSP_PIDNAMES command and gets the data instance."""
        return MspPidNames.parse(self._read_data(MSP_PIDNAMES))
    
    def get_raw_gps(self) -> MspRawGps:
        """Sends an MSP_RAW_GPS command and gets the data instance."""
        return MspRawGps.parse(self._read_data(MSP_RAW_GPS))
    
    def get_raw_imu(self) -> MspRawImu:
        """Sends an MSP_RAW_IMU command and gets the data instance."""
        return MspRawImu.parse(self._read_data(MSP_RAW_IMU))
    
    def get_rc(self) -> MspRc:
        """Sends an MSP_RC command and gets the data instance."""
        return MspRc.parse(self._read_data(MSP_RC))
    
    def get_rc_tuning(self) -> MspRcTuning:
        """Sends an MSP_RC_TUNING command and gets the data instance."""
        return MspRcTuning.parse(self._read_data(MSP_RC_TUNING))

    def get_servo(self) -> MspServo:
        """Sends an MSP_SERVO command and gets the data instance."""
        return MspServo.parse(self._read_data(MSP_SERVO))
    
    def get_servo_conf(self) -> MspServoConf:
        """Sends an MSP_SERVO_CONF command and gets the data instance."""
        return MspServoConf.parse(self._read_data(MSP_SERVO_CONF))
    
    def get_status(self) -> MspStatus:
        """Sends an MSP_STATUS command and gets the data instance."""
        return MspStatus.parse(self._read_data(MSP_STATUS))
    
    def get_waypoint(self) -> MspWaypoint:
        """Sends an MSP_WP command and gets the data instance."""
        return MspWaypoint.parse(self._read_data(MSP_WP))

    # --------------------------------- SET COMMAND METHODS ------------------------------------

    def bind(self) -> NoReturn:
        """Sends an MSP_BIND command.

        This command initiates the binding process between the transmitter (radio controller)
        and the receiver connected to the FC. Binding establishes a secure communication link
        between the transmitter (TX) and the receiver (RX).

        Note
        ----
        Ensure that the FC is ready to receive the bind command and that the transmitter is in
        binding mode before calling this method.
        """
        self._send_message(MSP_BIND)

    def calibrate_acc(self) -> NoReturn:
        """Sends an MSP_ACC_CALIBRATION command.

        This command initiates the accelerometer calibration process on the FC. Accelerometer
        calibration is essential for accurate attitude estimation and stabilization of the
        aircraft.

        Note
        ----
        The FC should be placed on a level surface during the calibration to ensure accurate
        results. Avoid moving or disturbing the FC during the process.
        """
        self._send_message(MSP_ACC_CALIBRATION)

    def calibrate_mag(self) -> NoReturn:
        """Sends an MSP_MAG_CALIBRATION command.

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

    def reset_conf(self) -> NoReturn:
        """Sends an MSP_RESET_CONF command.

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

    def set_box(self, data: tuple[MspBoxItem]) -> NoReturn:
        """Sends an MSP_SET_BOX command.

        Sets the flight modes (or "boxes") config on the FC. Flight modes define the behavior
        of the aircraft based on various inputs from the transmitter or other sources.

        Parameters
        ----------
        data : tuple[MspBoxItem]
            A tuple of non-null `MspBoxItem`s.
        """
        self._send_message(MSP_SET_BOX, data)

    def set_head(self, range: int) -> NoReturn:
        """Sends an MSP_SET_HEAD command.

        Sets the heading (yaw) direction reference on the FC with a value range of -180 to 180.
        It is used to define the forward direction of the aircraft relative to its orientation.

        Parameters
        ----------
        range : int
            The heading direction range value between -180 and 180.

        Raises
        ------
        ValueError
            If the provided range value is less than -180 or greater than 180.
        """
        if not -180 <= range <= 180:
            raise ValueError('Value must be within the range of -180 and 180.')

        self._send_message(MSP_SET_HEAD, data=(range,))

    def set_misc(self, data: MspSetMisc) -> NoReturn:
        """Sends an MSP_SET_MISC command.

        Sets miscellaneous config parameters on the FC—such as battery voltage scaling, failsafe
        behavior, or other settings not covered by specific MSP commands.

        Parameters
        ----------
        data : MspSetMisc
            An instance of the `MspSetMisc` class populated with values.
        """
        self._send_message(MSP_SET_MISC, data)

    def set_motor(self, data: MspMotor) -> NoReturn:
        """Sends an MSP_SET_MOTOR command.

        Sets the motor output values on the FC. Motor output values determine the throttle level
        for each motor, controlling the rotation speed and thrust generated by the motors.

        Parameters
        ----------
        data : MspMotor
            An instance of the `MspMotor` class populated with values.
        """
        self._send_message(MSP_SET_MOTOR, data)

    def set_pid(self, data: MspPid) -> NoReturn:
        """Sends an MSP_SET_PID command.

        Sets the PID values on the FC. PID values are used to adjust the stability and response
        characteristics of the aircraft.

        Parameters
        ----------
        data : MspPid
            An instance of the `MspPid` class populated with values.
        """
        self._send_message(MSP_SET_PID, data)

    def set_raw_gps(self, data: MspRawGps) -> NoReturn:
        """Sends an MSP_SET_RAW_GPS command.

        Sets the raw GPS data on the FC—such as the latitude, longitude, altitude, and other
        GPS-related information.

        Parameters
        ----------
        data : MspRawGps
            An instance of the `MspRawGps` class populated with values.
        """
        self._send_message(MSP_SET_RAW_GPS, data)

    def set_raw_rc(self, data: MspRc) -> NoReturn:
        """Sends an MSP_SET_RAW_RC command.

        Sets the raw receiver (RC/RX) channel data on the FC. Raw FC data includes the pulse
        width values received from the transmitter for each channel, typically representing
        control inputs such as throttle, pitch, roll, and yaw.

        Parameters
        ----------
        data : MspRc
            An instance of the `MspRc` class populated with values.
        """
        self._send_message(MSP_SET_RAW_RC, data)
    
    def set_rc_tuning(self, data: MspRcTuning) -> NoReturn:
        """Sends an MSP_SET_RC_TUNING command.

        Sets RC tuning parameters on the FC—such as expo, rates, and other settings related to
        RC control response and behavior.

        Parameters
        ----------
        data : MspRcTuning
            An instance of the `MspRcTuning` class populated with values.
        """
        self._send_message(MSP_SET_RC_TUNING, data)

    def set_servo_conf(self, data: tuple[MspServoConfItem]) -> NoReturn:
        """Sends an MSP_SET_SERVO_CONF command.

        Sets servo config parameters on the FC—such as servo mapping, direction, endpoints, and
        other settings related to servo control.
        
        Parameters
        ----------
        data : tuple[MspServoConfItem]
            A tuple with instances of the `MspServoConfItem` class populated with values.
        """
        self._send_message(MSP_SET_SERVO_CONF)

    def set_waypoint(self, data: MspWaypoint) -> NoReturn:
        """Sends an MSP_SET_WP command.

        Dispatches a command to set a waypoint on the FC, providing specific latitude, longitude,
        altitude, heading, duration and navigation flags for precise navigation and waypoint
        management.

        Parameters
        ----------
        data : MsWaypoint
            An instance of the `MspWaypoint` class populated with values.
        """
        self._send_message(MSP_SET_WP, data)

    def write_eeprom(self) -> NoReturn:
        """Sends an MSP_EEPROM_WRITE command.

        This command writes the current configuration settings to the EEPROM of the FC. 

        Note
        ----
        Writing to EEPROM should be done with caution, as it modifies the stored config
        directly. Ensure that the values written are valid and intended, as incorrect
        values could lead to unexpected behavior or instability.
        """
        self._send_message(MSP_EEPROM_WRITE)
