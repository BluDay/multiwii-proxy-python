"""
multiwii-proxy-python: A simple and user-friendly Python 3 module for MultiWii-based drones.

Formerly known as WiiProxy.

Copyright (C) 2024 BluDay

This module only supports communication through MSP v1 and not for any of the newer
versions. Consider using other libraries that uses MSP v2 and newer versions of the
protocol.

The re-write of this module was a great learning experience for me.
"""

__author__      = 'BluDay'
__copyrights__  = '© 2024 BluDay'
__credits__     = 'BluDay'
__description__ = 'A simple and user-friendly Python 3 module for MultiWii-based drones.'
__license__     = 'MIT'
__maintainer__  = 'BluDay'
__title__       = 'multiwii-proxy-python'
__url__         = 'https://bluday.github.io/multiwii-proxy-python'
__version__     = '3.0'

from ._command import _MspCommand

from .commands import (
    MSP_ACC_CALIBRATION,
    MSP_ALTITUDE,
    MSP_ANALOG,
    MSP_ATTITUDE,
    MSP_BIND,
    MSP_BOX,
    MSP_BOXIDS,
    MSP_BOXNAMES,
    MSP_COMP_GPS,
    MSP_EEPROM_WRITE,
    MSP_IDENT,
    MSP_MAG_CALIBRATION,
    MSP_MISC,
    MSP_MOTOR,
    MSP_MOTOR_PINS,
    MSP_PID,
    MSP_PIDNAMES,
    MSP_RAW_GPS,
    MSP_RAW_IMU,
    MSP_RC,
    MSP_RC_TUNING,
    MSP_RESET_CONF,
    MSP_SELECT_SETTING,
    MSP_SERVO,
    MSP_SERVO_CONF,
    MSP_SET_BOX,
    MSP_SET_HEAD,
    MSP_SET_MISC,
    MSP_SET_MOTOR,
    MSP_SET_PID,
    MSP_SET_RAW_GPS,
    MSP_SET_RAW_RC,
    MSP_SET_RC_TUNING,
    MSP_SET_SERVO_CONF,
    MSP_SET_WP,
    MSP_STATUS,
    MSP_WP
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
    MspSetMisc,
    MspStatus,
    MspWaypoint
)

from .messaging import (
    _crc8_xor,
    _create_request_message,
    _MspResponseMessage,
    _parse_response_message,
    MESSAGE_ERROR_HEADER,
    MESSAGE_INCOMING_HEADER,
    MspMessageError
)

from serial import Serial

from time import perf_counter, sleep

from typing import Any, Final, NoReturn, Type

class MultiWii(object):
    """
    The main class for wiiproxy that handles communication with MultiWii flight controllers.
    
    This class requires an open serial port with a baudrate of 115200 to be passed at
    instantiation.

    Note
    ----
    This class supports MSP v1 and does not support any newer versions.

    Note
    ----
    This class can be imported directly through the main module.
    """
    DEFAULT_MESSAGE_WRITE_READ_DELAY: Final[float] = 0.005
    """float: The default delay in seconds between writing and reading messages."""

    MSP_VERSION: Final[int] = 1
    """int: The supported MultiWii Serial Protocol version."""

    _message_write_read_delay: float

    _serial_port: Final[Serial]

    def __init__(self, serial_port: Serial) -> NoReturn:
        """
        Initializes an instance using the provided serial port.

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
        if not isinstance(serial_port, Serial):
            raise TypeError('The serial port must be an instance of "Serial".')

        self._command_to_data_structure_type_map = {
            MSP_ALTITUDE:   MspAltitude,
            MSP_ANALOG:     MspAnalog,
            MSP_ATTITUDE:   MspAttitude,
            MSP_BOX:        MspBox,
            MSP_BOXIDS:     MspBoxIds,
            MSP_BOXNAMES:   MspBoxNames,
            MSP_COMP_GPS:   MspCompGps,
            MSP_IDENT:      MspIdent,
            MSP_MISC:       MspMisc,
            MSP_MOTOR:      MspMotor,
            MSP_MOTOR_PINS: MspMotorPins,
            MSP_PID:        MspPid,
            MSP_PIDNAMES:   MspPidNames,
            MSP_RAW_GPS:    MspRawGps,
            MSP_RAW_IMU:    MspRawImu,
            MSP_RC:         MspRc,
            MSP_RC_TUNING:  MspRcTuning,
            MSP_SERVO:      MspServo,
            MSP_SERVO_CONF: MspServoConf,
            MSP_STATUS:     MspStatus,
            MSP_WP:         MspWaypoint
        }

        self._message_write_read_delay = self.DEFAULT_MESSAGE_WRITE_READ_DELAY

        self._serial_port = serial_port

    @property
    def command_to_data_structure_type_map(self) -> dict[_MspCommand, Type]:
        """
        Gets the command to data structure type dictionary.

        Returns
        -------
        dict[_MspCommand, Type]
            A instance with a copy of the map.
        """
        return dict(self._command_to_data_structure_type_map)
    
    @property
    def message_write_read_delay(self) -> float:
        """
        Gets the delay (in seconds) between each write and read message.

        Returns
        -------
        float
            The delay in seconds.
        """
        return self._message_write_read_delay

    @property
    def serial_port(self) -> Serial:
        """
        Gets the serial port instance.

        Returns
        -------
        Serial
            The serial port instance.
        """
        return self._serial_port

    @message_write_read_delay.setter
    def message_write_read_delay(self, value: float) -> NoReturn:
        """
        Sets the delay (in seconds) between each write and read command.

        This property controls the delay between each write message followed by a read message
        sent to the FC. A message with empty data values is sent first, followed by a delay,
        and then a read message to retrieve information from the FC.

        Parameters
        ----------
        value : float
            The delay in seconds.

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

    def _read_response_message(self, command: _MspCommand) -> _MspResponseMessage:
        """
        Reads a message using the specified MSP command.

        Note
        ----
        This method sends a write message with empty values to the FC in order to retrieve a
        response message. Ensure that the FC is ready to to respond to the command code sent.

        Parameters
        ----------
        command : _MspCommand
            An instance of `_MspCommand` representing the MSP command used to read the message.

        Raises
        ------
        MspMessageError
            If an error message is returned from the FC.

        Returns
        -------
        _MspResponseMessage
            A named tuple with the command, parsed data and additional information.
        """
        try:
            self._send_request_message(command)

            sleep(self._message_write_read_delay)

            header = self._serial_port.read(3)

            if header == MESSAGE_ERROR_HEADER:
                raise MspMessageError('An error has occured.') 

            if header != MESSAGE_INCOMING_HEADER:
                raise MspMessageError('Invalid incoming message preamble received.')

            command_code = self._serial_port.read(1)

            if command_code[0] != command.code:
                raise MspMessageError(
                    'Invalid command code detected. ({}, {})'.format(
                        command.code,
                        command_code
                    )
                )

            payload = bytes()

            payload += command_code

            data_size = self._serial_port.read(1)
            data      = self._serial_port.read(data_size[0])

            payload += data_size
            payload += data

            checksum = self._serial_port.read(1)

            if checksum[0] != _crc8_xor(payload):
                raise MspMessageError(f'Invalid payload checksum detected for {command}.')
        
            return _parse_response_message(command, payload)
        finally:
            self._serial_port.reset_input_buffer()

    def _send_request_message(self, command: _MspCommand, data: tuple[int] = ()) -> NoReturn:
        """
        Sends a message with the specified MSP command and optional data values.

        Parameters
        ----------
        command : _MspCommand
            An instance of `_MspCommand` representing the MSP command used to write the message.
        data : tuple[int]
            Data values to serialize and include in the message payload.
        """
        try:
            self._serial_port.write(_create_request_message(command, data))
        finally:
            self._serial_port.reset_output_buffer()

    def arm(self) -> NoReturn:
        """
        Arms the vehicle.

        This method prepares the vehicle for operation by simulating the arming sequence
        performed by physical transmitters. It sets the throttle value to its minimum, and
        the yaw value to its maximum, for a few seconds simultaneously to initiate the arming
        process. This ensures that the vehicle is ready for further commands and a safe flight.

        Note
        ----
        Ensure that the vehicle is in a safe enviornment and that conditions are suitable for
        arming before invoking this method.
        """
        data = MspRc(
            roll=1500,
            pitch=1500,
            yaw=2000,
            throttle=1000,
            aux1=0,
            aux2=0,
            aux3=0,
            aux4=0
        )

        start_time = perf_counter()

        elapsed_time = 0

        while elapsed_time < 0.5:
            self.set_raw_rc(data)

            sleep(0.05)

            elapsed_time = perf_counter() - start_time

    def bind_transmitter_and_receiver(self) -> NoReturn:
        """
        Sends an MSP_BIND command.

        This command initiates the binding process between the transmitter (radio controller)
        and the receiver connected to the FC. Binding establishes a secure communication link
        between the transmitter (TX) and the receiver (RX).

        Note
        ----
        Ensure that the FC is ready to receive the bind command and that the transmitter is in
        binding mode before calling this method.
        """
        self._send_request_message(MSP_BIND)

    def calibrate_accelerometer(self) -> NoReturn:
        """
        Sends an MSP_ACC_CALIBRATION command.

        This command initiates the accelerometer calibration process on the FC. Accelerometer
        calibration is essential for accurate attitude estimation and stabilization of the
        aircraft.

        Note
        ----
        The FC should be placed on a level surface during the calibration to ensure accurate
        results. Avoid moving or disturbing the FC during the process.
        """
        self._send_request_message(MSP_ACC_CALIBRATION)

    def calibrate_magnetometer(self) -> NoReturn:
        """
        Sends an MSP_MAG_CALIBRATION command.

        This command initiates the magnetometer (compass) calibration process on the FC.
        Magnetometer calibration is crucial for accurate heading estimation and navigation,
        especially in GPS-assisted flight modes.

        Note
        ----
        The FC should be rotated along all three axes (roll, pitch, yaw) in a smooth and
        consistent manner to ensure accurate results. Avoid any magnetic interference or
        disturbances during the process.
        """
        self._send_request_message(MSP_ACC_CALIBRATION)

    def disarm(self) -> NoReturn:
        """
        Disarms the vehicle.

        This method safely disarms the vehicle by resetting the yaw and throttle to their minimum
        values. This process simulates the disarming sequence used by physical transmitters,
        ensuring that the vehicle is no longer ready for flight, and that the vehicle is in a
        more safe state.

        Note
        ----
        Always ensure that the vehicle is on the ground and stationary before invoking this
        method to avoid accidental movement or damage.
        """
        data = MspRc(
            roll=1500,
            pitch=1500,
            yaw=1000,
            throttle=1000,
            aux1=0,
            aux2=0,
            aux3=0,
            aux4=0
        )

        start_time = perf_counter()

        elapsed_time = 0

        while elapsed_time < 0.5:
            self.set_raw_rc(data)

            sleep(0.05)

            elapsed_time = perf_counter() - start_time

    def get_data(self, command: _MspCommand) -> Any:
        """
        Sends a given command to the FC and parses the retrieved data values.

        Parameters
        ----------
        command : _MspCommand
            An instance of `_MspCommand` representing the MSP command to get corresponding data
            values for.

        Returns
        -------
        Any
            An instance of a corresponding data structure type for the given command.
        """
        data = self._read_response_message(command).data

        return self._command_to_data_structure_type_map[command].parse(data)

    def reset_config(self) -> NoReturn:
        """
        Sends an MSP_RESET_CONF command.

        This command resets the configuration settings on the FC to their default values.
        It effectively restores the FC to its initial configuration state, clearing any
        customized settings or adjustments made by the user.

        Note
        ----
        Resetting the config should be done with caution, as it will revert all settings to
        their defaults. Make sure to reconfigure the FC according to your requirements after
        executing this command.
        """
        self._send_request_message(MSP_RESET_CONF)

    def save_config_to_eeprom(self) -> NoReturn:
        """
        Sends an MSP_EEPROM_WRITE command.

        This command writes the current configuration settings to the EEPROM of the FC. 

        Note
        ----
        Writing to EEPROM should be done with caution, as it modifies the stored config
        directly. Ensure that the values written are valid and intended, as incorrect
        values could lead to unexpected behavior or instability.
        """
        self._send_request_message(MSP_EEPROM_WRITE)

    def select_setting(self, value: int) -> NoReturn:
        """
        Sends an MSP_SELECT_SETTING command.

        Selects the "setting configuration" with different PID and rate values using the given
        range value.

        Parameters
        ----------
        value : int
            A value of 0, 1 or 2.

        Raises
        ------
        ValueError
            If the provided value is not 0, 1 or 2.
        """
        if not value in (0, 1, 2):
            raise ValueError('Value must be 0, 1 or 2.')

        self._send_request_message(MSP_SELECT_SETTING, data=(value,))

    def set_boxes(self, data: MspBox) -> NoReturn:
        """
        Sends an MSP_SET_BOX command.

        Sets the flight modes (or "boxes") config on the FC. Flight modes define the behavior
        of the aircraft based on various inputs from the transmitter or other sources.

        Parameters
        ----------
        data : tuple[MspBoxItem]
            A tuple of non-null `MspBoxItem` values.
        """
        self._send_request_message(MSP_SET_BOX, data.as_serializable())

    def set_head(self, value: int) -> NoReturn:
        """
        Sends an MSP_SET_HEAD command.

        Sets the heading (yaw) direction reference on the FC with a value range of -180 to 180.
        It is used to define the forward direction of the aircraft relative to its orientation.

        Parameters
        ----------
        range : int
            The heading direction value within a range of -180 and 180.

        Raises
        ------
        ValueError
            If the provided range value is less than -180 or greater than 180.
        """
        if not -180 <= value <= 180:
            raise ValueError('Value must be within the range of -180 and 180.')

        self._send_request_message(MSP_SET_HEAD, data=(value,))

    def set_misc_config(self, data: MspSetMisc) -> NoReturn:
        """
        Sends an MSP_SET_MISC command.

        Sets miscellaneous config parameters on the FC—such as battery voltage scaling, failsafe
        behavior, or other settings not covered by specific MSP commands.

        Parameters
        ----------
        data : MspSetMisc
            An instance of the `MspSetMisc` class populated with values.
        """
        self._send_request_message(MSP_SET_MISC, data.as_serializable())

    def set_motors(self, data: MspMotor) -> NoReturn:
        """
        Sends an MSP_SET_MOTOR command.

        Sets the motor output values on the FC. Motor output values determine the throttle level
        for each motor, controlling the rotation speed and thrust generated by the motors.

        Parameters
        ----------
        data : MspMotor
            An instance of the `MspMotor` class populated with values.
        """
        self._send_request_message(MSP_SET_MOTOR, data.as_serializable())

    def set_pid_values(self, data: MspPid) -> NoReturn:
        """
        Sends an MSP_SET_PID command.

        Sets the PID values on the FC. PID values are used to adjust the stability and response
        characteristics of the aircraft.

        Parameters
        ----------
        data : MspPid
            An instance of the `MspPid` class populated with values.
        """
        self._send_request_message(MSP_SET_PID, data.as_serializable())

    def set_raw_gps(self, data: MspRawGps) -> NoReturn:
        """
        Sends an MSP_SET_RAW_GPS command.

        Sets the raw GPS data on the FC—such as the latitude, longitude, altitude, and other
        GPS-related information.

        Parameters
        ----------
        data : MspRawGps
            An instance of the `MspRawGps` class populated with values.
        """
        self._send_request_message(MSP_SET_RAW_GPS, data.as_serializable())

    def set_raw_rc(self, data: MspRc) -> NoReturn:
        """
        Sends an MSP_SET_RAW_RC command.

        Sets the raw receiver (RC/RX) channel data on the FC. Raw FC data includes the pulse
        width values received from the transmitter for each channel, typically representing
        control inputs such as throttle, pitch, roll, and yaw.

        Parameters
        ----------
        data : MspRc
            An instance of the `MspRc` class populated with values.
        """
        self._send_request_message(MSP_SET_RAW_RC, data.as_serializable())
    
    def set_rc_tuning(self, data: MspRcTuning) -> NoReturn:
        """
        Sends an MSP_SET_RC_TUNING command.

        Sets RC tuning parameters on the FC—such as expo, rates, and other settings related to
        RC control response and behavior.

        Parameters
        ----------
        data : MspRcTuning
            An instance of the `MspRcTuning` class populated with values.
        """
        self._send_request_message(MSP_SET_RC_TUNING, data.as_serializable())

    def set_servo_config(self, data: MspServoConf) -> NoReturn:
        """
        Sends an MSP_SET_SERVO_CONF command.

        Sets servo config parameters on the FC—such as servo mapping, direction, endpoints, and
        other settings related to servo control.
        
        Parameters
        ----------
        data : tuple[MspServoConfItem]
            A tuple with instances of the `MspServoConfItem` class populated with values.
        """
        self._send_request_message(MSP_SET_SERVO_CONF, data.as_serializable())

    def set_waypoint(self, data: MspWaypoint) -> NoReturn:
        """
        Sends an MSP_SET_WP command.

        Dispatches a command to set a waypoint on the FC, providing specific latitude, longitude,
        altitude, heading, duration and navigation flags for precise navigation and waypoint
        management.

        Parameters
        ----------
        data : MsWaypoint
            An instance of the `MspWaypoint` class populated with values.
        """
        self._send_request_message(MSP_SET_WP, data.as_serializable())
