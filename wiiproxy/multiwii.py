from . import MspData

from .config import CommandPriority

from .data import (
    MspSetMotor,
    MspSetRawGps,
    MspSetRawRc,
    MspSetRcTuning,
    MspSetPid,
    MspSetBoxItem,
    MspSetMisc,
    MspSetWaypoint,
    MspSetServoConfItem
)

from .msp_commands import (
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

from serial    import Serial
from time      import sleep
from threading import Thread
from typing    import Dict, Final, NoReturn

class MultiWii(object):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial port—with a baudrate of 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    DEFAULT_MESSAGE_WRITE_READ_DELAY: Final[float] = 0.005

    MSP_VERSION: Final[str] = 'v1'

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _command_priorities: Final[Dict[int, CommandPriority]]

    _data: Final[MspData]

    _is_active: bool

    _message_write_read_delay: float

    _serial: Final[Serial]

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

        self._command_priorities = {}

        self._data = MspData()

        self._is_active = False

        self._message_write_read_delay = MultiWii.DEFAULT_MESSAGE_WRITE_READ_DELAY

        self._serial = serial

        self.reset_command_priorities()
        self.reset_data()

    # --------------------------------------- PROPERTIES ---------------------------------------
    
    @property
    def data(self) -> MspData:
        """Gets the MSP data collection instance."""
        return self._data

    @property
    def is_active(self) -> bool:
        """Gets a value indicating whether the worker thread is active or not."""
        return self._is_active

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

    def _read_message(self, command: int) -> bytes:
        """Reads a message from the FC with the specified command code.

        Note
        ----
        This method sends a write message with empty values to the FC in order to retrieve a
        response message. Ensure that the FC is ready to to respond to the command code sent.

        Raises
        ------
        ValueError
            If the provided command code is invalid or not recognized.
        TimeoutError
            If a timeout occurs while waiting for the message from the FC.
        """
        pass

    def _send_message(self, command: int, data: tuple[int] = None) -> NoReturn:
        """Sends a message to the FC with the specified command code and optional data values.

        Raises
        ------
        ValueError
            If the provided command code is invalid or not recognized.
        TimeoutError
            If a timeout occurs while waiting for the FC to acknowledge the message.
        """
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

    def set_box(self, values: tuple[MspSetBoxItem]) -> NoReturn:
        """Sends the MSP_SET_BOX

        Sets the flight modes (or "boxes") config on the FC. Flight modes define the behavior
        of the aircraft based on various inputs from the transmitter or other sources.
        """
        self._send_message(MSP_SET_BOX)

    def set_head(self, range: int) -> NoReturn:
        """Sends the MSP_SET_HEAD command.

        Sets the heading (yaw) direction reference on the FC. It is used to define the forward
        direction of the aircraft relative to its orientation.
        """
        self._send_message(MSP_SET_HEAD)

    def set_misc(self, values: MspSetMisc) -> NoReturn:
        """Sends the MSP_SET_MISC command.

        Sets miscellaneous config parameters on the FC—such as battery voltage scaling, failsafe
        behavior, or other settings not covered by specific MSP commands.
        """
        self._send_message(MSP_SET_MISC)

    def set_motor(self, values: MspSetMotor) -> NoReturn:
        """Sends the MSP_SET_MOTOR command.

        Sets the motor output values on the FC. Motor output values determine the throttle level
        for each motor, controlling the rotation speed and thrust generated by the motors.
        """
        self._send_message(MSP_SET_MOTOR)

    def set_pid(self, values: MspSetPid) -> NoReturn:
        """Sends the MSP_SET_PID command.

        Sets the PID values on the FC. PID values are used to adjust the stability and response
        characteristics of the aircraft.
        """
        self._send_message(MSP_SET_PID)

    def set_raw_gps(self, values: MspSetRawGps) -> NoReturn:
        """Sends the MSP_SET_RAW_GPS command.

        Sets the raw GPS data on the FC—such as the latitude, longitude, altitude, and other
        GPS-related information.
        """
        self._send_message(MSP_SET_RAW_GPS)

    def set_raw_rc(self, values: MspSetRawRc) -> NoReturn:
        """Sends the MSP_SET_RAW_RC command.

        Sets the raw receiver (RC/RX) channel data on the FC. Raw FC data includes the pulse
        width values received from the transmitter for each channel, typically representing
        control inputs such as throttle, pitch, roll, and yaw.
        """
        self._send_message(MSP_SET_RAW_RC)
    
    def set_rc_tuning(self, values: MspSetRcTuning) -> NoReturn:
        """Sends the MSP_SET_RC_TUNING command.

        Sets RC tuning parameters on the FC—such as expo, rates, and other settings related to
        RC control response and behavior.
        """
        self._send_message(MSP_SET_RC_TUNING)

    def set_servo_conf(self, values: tuple[MspSetServoConfItem]) -> NoReturn:
        """Sends the MSP_SET_SERVO_CONF command.

        Sets servo config parameters on the FC—such as servo mapping, direction, endpoints, and
        other settings related to servo control.
        """
        self._send_message(MSP_SET_SERVO_CONF)

    def set_waypoint(self, values: MspSetWaypoint) -> NoReturn:
        """Sends the MSP_SET_WP command.

        Dispatches a command to set a waypoint on the FC, providing specific latitude, longitude,
        altitude, heading, duration and navigation flags for precise navigation and waypoint
        management.
        """
        self._send_message(MSP_SET_WP)

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

    def get_command_priorities(self) -> Dict[int, CommandPriority]:
        """Gets all priorities for the provided read-command."""
        return dict(self._command_priorities)

    def get_command_priority(self, command: int) -> CommandPriority:
        """Gets the priority for the provided read-command."""
        return self._command_priorities[command]

    def reset_command_priorities(self) -> NoReturn:
        """Resets priorities for all read-command codes to their default value."""
        self._command_priorities = {
            MSP_ALTITUDE:   CommandPriority.High,
            MSP_ANALOG:     CommandPriority.Medium,
            MSP_ATTITUDE:   CommandPriority.High,
            MSP_BOX:        CommandPriority.Low,
            MSP_BOXIDS:     CommandPriority.Low,
            MSP_BOXNAMES:   CommandPriority.Low,
            MSP_COMP_GPS:   CommandPriority.Inactive,
            MSP_IDENT:      CommandPriority.Low,
            MSP_MISC:       CommandPriority.Low,
            MSP_MOTOR:      CommandPriority.High,
            MSP_MOTOR_PINS: CommandPriority.Low,
            MSP_PID:        CommandPriority.Low,
            MSP_PIDNAMES:   CommandPriority.Low,
            MSP_RAW_GPS:    CommandPriority.Inactive,
            MSP_RAW_IMU:    CommandPriority.High,
            MSP_RC:         CommandPriority.Critical,
            MSP_RC_TUNING:  CommandPriority.Low,
            MSP_SERVO:      CommandPriority.Medium,
            MSP_SERVO_CONF: CommandPriority.Low,
            MSP_STATUS:     CommandPriority.Medium,
            MSP_WP:         CommandPriority.Inactive
        }

    def reset_data(self) -> NoReturn:
        """Resets all data values."""
        self._data._reset()

    def set_command_priority(self, command: int, priority: CommandPriority) -> NoReturn:
        """Sets the priority for the provided read-command."""
        self._command_priorities[command] = priority

    def start_worker(self) -> NoReturn:
        """Starts the worker thread."""
        pass

    def stop_worker(self) -> NoReturn:
        """Stops the worker thread."""
        pass
