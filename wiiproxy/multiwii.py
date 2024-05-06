from . import (
    MultiWiiData,
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

from serial import Serial
from time   import sleep
from typing import Final, NoReturn

class MultiWii(MultiWiiData):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial port—with a baudrate of 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default delay (in seconds) for serial writes."""
    DEFAULT_COMMAND_WRITE_READ_DELAY: Final[float] = 0.005

    """The MSP version used."""
    MSP_VERSION: Final[str] = 'v1'

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _command_write_read_delay: int

    _serial: Serial

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial port.

        This constructor initializes a new instance of the MultiWii class using the provided
        serial port for communication with the FC. It sets up the initial state of the object,
        including the activation status, command write-read delay and serial port configuration.
        Additionally, it ensures that the provided serial port is of the correct type (Serial).
        If the serial port is not of the expected type, a TypeError is raised.
        """
        if not isinstance(serial, Serial):
            raise TypeError('"serial" must be an instance of "Serial".')

        self._is_active = False

        self._command_write_read_delay = MultiWii.DEFAULT_COMMAND_WRITE_READ_DELAY

        self._serial = serial

        super().reset()

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def command_write_read_delay(self) -> float:
        """Gets the delay (in seconds) between each write and read command."""
        return self._command_write_read_delay

    @property
    def serial(self) -> Serial:
        """Gets the used serial instance that was provided at instantiation."""
        return self._serial

    @command_write_read_delay.setter
    def command_write_read_delay(self, value: float) -> NoReturn:
        """Sets the delay (in seconds) between each write and read command.

        This property controls the delay between each write command followed by a read command
        sent to the FC. A write command with empty data values is sent first to prepare the FC,
        followed by a delay, and then a read command to retrieve information from the FC.

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
            
        self._command_write_read_delay = value

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

    def _get_data(self, command: int) -> bytes:
        """Reads a message of a command code and returns parsed data values."""
        pass

    def _parse_data(self, command: int, message: bytes) -> tuple[int]:
        """Parses data from a received or sent message."""
        pass

    def _read_message(self, command: int) -> bytes:
        """Reads a message of a command code from the FC."""
        pass

    def _send_message(self, command: int, data: tuple[int] = None) -> NoReturn:
        """Sends a message of a specified command and data values to the FC."""
        pass

    # ------------------------------------- SET COMMANDS ---------------------------------------

    def bind(self) -> NoReturn:
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

    def calibrate_acc(self) -> NoReturn:
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

    def calibrate_mag(self) -> NoReturn:
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

    def reset_conf(self) -> NoReturn:
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

    def write_eeprom(self) -> NoReturn:
        """Sends the MSP_EEPROM_WRITE command.

        This command writes the current configuration settings to the EEPROM of the FC. 

        Note
        ----
        Writing to EEPROM should be done with caution, as it modifies the stored config
        directly. Ensure that the values written are valid and intended, as incorrect
        values could lead to unexpected behavior or instability.
        """
        self._send_message(MSP_EEPROM_WRITE)

    # ------------------------------------- CORE METHODS ---------------------------------------

    def start(self) -> NoReturn:
        """Starts the worker thread."""
        pass

    def stop(self) -> NoReturn:
        """Stops the worker thread."""
        pass
