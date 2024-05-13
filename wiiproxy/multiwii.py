from ._serialization import (
    read_int8_le,
    read_int16_le,
    read_int32_le,
    read_uint8_le,
    read_uint16_le,
    read_uint32_le,
    write_int8_le,
    write_int16_le,
    write_int32_le,
    write_uint8_le,
    write_uint16_le,
    write_uint32_le
)

from .msp_config import (
    MultiWiiMultitype,
    MultiWiiCapability
)

from .msp_data import (
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
    MspWaypoint,
    BoxItem,
    Misc,
    ServoConfItem
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

from serial import Serial
from time   import sleep
from typing import Any, Final, NoReturn

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

    NAME_SEPARATION_CHAR: Final[str] = ';'

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

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

        self._message_write_read_delay = MultiWii.DEFAULT_MESSAGE_WRITE_READ_DELAY

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

    def _decode_names(self, data: bytes) -> tuple[str]:
        """Decodes the deserialized string value and splits it to a tuple."""
        return tuple(data.decode('ascii').split(MultiWii.NAME_SPARATION_CHAR))

    def _read_message_data(self, command: int) -> bytes:
        """Reads a message and returns the raw data bytes."""
        return self._read_message(command)[5:-1]

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

    # ------------------------------------- GET COMMANDS ---------------------------------------

    def get_altitude(self) -> MspAltitude:
        """Sends the MSP_ALTITUDE command and gets the data instance."""
        data = self._read_message_data(MSP_ALTITUDE)

        return MspAltitude(
            estimation         = read_int32_le(data),
            pressure_variation = read_int16_le(data, offset=4)
        )
    
    def get_analog(self) -> MspAnalog:
        """Sends the MSP_ANALOG command and gets the data instance."""
        data = self._read_message_data(MSP_ANALOG)

        return MspAnalog(
            voltage         = read_uint8_le(data),
            power_meter_sum = read_uint16_le(data, offset=1),
            rssi            = read_uint16_le(data, offset=3),
            amperage        = read_uint16_le(data, offset=5)
        )
    
    def get_attitude(self) -> MspAttitude:
        """Sends the MSP_ATTITUDE command and gets the data instance."""
        data = self._read_message_data(MSP_ATTITUDE)

        return MspAttitude(
            angle_x = read_int16_le(data),
            angle_y = read_int16_le(data, offset=2),
            heading = read_int16_le(data, offset=4)
        )
    
    def get_box(self) -> MspBox:
        """Sends the MSP_BOX command and gets the data instance."""
        data = self._read_message_data(MSP_BOX)

        values = ()

        for offset in range(len(data), step=2):
            values += (read_int16_le(data, offset),)
        
        return MspBox(values)
    
    def get_box_ids(self) -> MspBoxIds:
        """Sends the MSP_BOXIDS command and gets the data instance."""
        data = self._read_message_data(MSP_BOXIDS)

        values = ()

        for offset in range(len(data)):
            values += (read_int8_le(data, offset),)

        return MspBoxIds(values)
    
    def get_box_names(self) -> MspBoxNames:
        """Sends the MSP_BOXNAMES command and gets the data instance."""
        data = self._read_message_data(MSP_BOXNAMES)

        return MspBoxNames(names=self._decode_names(data))
    
    def get_comp_gps(self) -> MspCompGps:
        """Sends the MSP_COMP_GPS command and gets the data instance."""
        data = self._read_message_data(MSP_COMP_GPS)

        return MspCompGps(
            distance_to_home  = read_uint16_le(data),
            direction_to_home = read_uint16_le(data, offset=2),
            update            = read_uint8_le(data, offset=4)
        )
    
    def get_ident(self) -> MspIdent:
        """Sends the MSP_IDENT command and gets the data instance."""
        data = self._read_message_data(MSP_IDENT)

        return MspIdent(
            version      = read_uint8_le(data),
            multitype    = MultiWiiMultitype(read_uint8_le(data, offset=1)),
            capabilities = MultiWiiCapability.get_capabilities(read_uint8_le(data, offset=2)),
            navi_version = read_uint32_le(data, offset=3)
        )
    
    def get_misc(self) -> MspMisc:
        """Sends the MSP_MISC command and gets the data instance."""
        data = self._read_message_data(MSP_MISC)

        return MspMisc(
            power_trigger     = read_uint16_le(data),
            throttle_failsafe = read_uint16_le(data, offset=2),
            throttle_idle     = read_uint16_le(data, offset=4),
            throttle_min      = read_uint16_le(data, offset=6),
            throttle_max      = read_uint16_le(data, offset=8),
            plog_arm          = read_uint16_le(data, offset=10),
            plog_lifetime     = read_uint32_le(data, offset=12),
            mag_declination   = read_uint16_le(data, offset=16),
            battery_scale     = read_uint8_le(data, offset=18),
            battery_warn_1    = read_uint8_le(data, offset=19),
            battery_warn_2    = read_uint8_le(data, offset=20),
            battery_critical  = read_uint8_le(data, offset=21)
        )
    
    def get_motor(self) -> MspMotor:
        """Sends the MSP_MOTOR command and gets the data instance."""
        data = self._read_message_data(MSP_MOTOR)

        return MspMotor(
            motor1=read_uint16_le(data),
            motor2=read_uint16_le(data, offset=2),
            motor3=read_uint16_le(data, offset=4),
            motor4=read_uint16_le(data, offset=6),
            motor5=read_uint16_le(data, offset=8),
            motor6=read_uint16_le(data, offset=10),
            motor7=read_uint16_le(data, offset=12),
            motor8=read_uint16_le(data, offset=14)
        )
    
    def get_motor_pins(self) -> MspMotorPins:
        """Sends the MSP_MOTOR_PINS command and gets the data instance."""
        data = self._read_message_data(MSP_MOTOR_PINS)

        values = ()

        for offset in range(8):
            values += (read_int8_le(data, offset),)

        return MspMotorPins(values)
    
    def get_pid(self) -> MspPid:
        """Sends the MSP_PID command and gets the data instance."""
        data = self._read_message_data(MSP_PID) 

        return MspPid(
            roll_p=read_uint8_le(data),
            roll_i=read_uint8_le(data, offset=1),
            roll_d=read_uint8_le(data, offset=2),

            pitch_p=read_uint8_le(data, offset=3),
            pitch_i=read_uint8_le(data, offset=4),
            pitch_d=read_uint8_le(data, offset=5),

            yaw_p=read_uint8_le(data, offset=6),
            yaw_i=read_uint8_le(data, offset=7),
            yaw_d=read_uint8_le(data, offset=8),

            alt_p=read_uint8_le(data, offset=9),
            alt_i=read_uint8_le(data, offset=10),
            alt_d=read_uint8_le(data, offset=11),

            pos_p=read_uint8_le(data, offset=12),
            pos_i=read_uint8_le(data, offset=13),
            pos_d=read_uint8_le(data, offset=14),

            posr_p=read_uint8_le(data, offset=15),
            posr_i=read_uint8_le(data, offset=16),
            posr_d=read_uint8_le(data, offset=17),

            navr_p=read_uint8_le(data, offset=18),
            navr_i=read_uint8_le(data, offset=19),
            navr_d=read_uint8_le(data, offset=20),

            level_p=read_uint8_le(data, offset=21),
            level_i=read_uint8_le(data, offset=22),
            level_d=read_uint8_le(data, offset=23),

            mag_p=read_uint8_le(data, offset=24),
            mag_i=read_uint8_le(data, offset=25),
            mag_d=read_uint8_le(data, offset=26),

            vel_p=read_uint8_le(data, offset=27),
            vel_i=read_uint8_le(data, offset=28),
            vel_d=read_uint8_le(data, offset=29)
        )
    
    def get_pid_names(self) -> MspPidNames:
        """Sends the MSP_PIDNAMES command and gets the data instance."""
        data = self._read_message_data(MSP_PIDNAMES)

        return MspPidNames(names=self._decode_names(data))
    
    def get_raw_gps(self) -> MspRawGps:
        """Sends the MSP_RAW_GPS command and gets the data instance."""
        data = self._read_message_data(MSP_RAW_GPS)

        return MspRawGps(
            fix           = read_uint8_le(data),
            satellites    = read_uint8_le(data, offset=1),
            latitude      = read_uint32_le(data, offset=2),
            longitude     = read_uint32_le(data, offset=6),
            altitude      = read_uint16_le(data, offset=10),
            speed         = read_uint16_le(data, offset=12),
            ground_course = read_uint16_le(data, offset=14)
        )
    
    def get_raw_imu(self) -> MspRawImu:
        """Sends the MSP_RAW_IMU command and gets the data instance."""
        data = self._read_message_data(MSP_RAW_IMU)

        return MspRawImu(
            acc_x=float(read_int16_le(data)),
            acc_y=float(read_int16_le(data, offset=2)),
            acc_z=float(read_int16_le(data, offset=4)),

            gyro_x=float(read_int16_le(data, offset=6)),
            gyro_y=float(read_int16_le(data, offset=8)),
            gyro_z=float(read_int16_le(data, offset=10)),

            mag_x=float(read_int16_le(data, offset=12)),
            mag_y=float(read_int16_le(data, offset=14)),
            mag_z=float(read_int16_le(data, offset=16))
        )
    
    def get_rc(self) -> MspRc:
        """Sends the MSP_RC command and gets the data instance."""
        data = self._read_message_data(MSP_RC)

        return MspRc(
            roll     = read_uint16_le(data),
            pitch    = read_uint16_le(data, offset=2),
            yaw      = read_uint16_le(data, offset=4),
            throttle = read_uint16_le(data, offset=6),
            aux1     = read_uint16_le(data, offset=8),
            aux2     = read_uint16_le(data, offset=10),
            aux3     = read_uint16_le(data, offset=12),
            aux4     = read_uint16_le(data, offset=14)
        )
    
    def get_rc_tuning(self) -> MspRcTuning:
        """Sends the MSP_RC_TUNING command and gets the data instance."""
        data = self._read_message_data(MSP_RC_TUNING)

        return MspRcTuning(
            rate                 = read_uint8_le(data),
            expo                 = read_uint8_le(data, offset=1),
            roll_pitch_rate      = read_uint8_le(data, offset=2),
            yaw_rate             = read_uint8_le(data, offset=3),
            dynamic_throttle_pid = read_uint8_le(data, offset=4),
            throttle_mid         = read_uint8_le(data, offset=5),
            throttle_expo        = read_uint8_le(data, offset=6)
        )
    
    def get_servo(self) -> MspServo:
        """Sends the MSP_SERVO command and gets the data instance."""
        data = self._read_message_data(MSP_SERVO)

        values = ()

        for offset in range(len(data), step=2):
            values += (read_int16_le(data, offset),)

        return MspServo(values)
    
    def get_servo_conf(self) -> MspServoConf:
        """Sends the MSP_SERVO_CONF command and gets the data instance."""
        data = self._read_message_data(MSP_SERVO_CONF)

        values = ()

        for offset in range(len(data), step=7):
            item = ServoConfItem(
                min    = read_uint16_le(data, offset),
                max    = read_uint16_le(data, offset + 2),
                middle = read_uint16_le(data, offset + 4),
                rate   = read_uint8_le(data, offset + 5)
            )

            values += (item,)

        return MspServoConf(values)
    
    def get_status(self) -> MspStatus:
        """Sends the MSP_STATUS command and gets the data instance."""
        data = self._read_message_data(MSP_STATUS)

        return MspStatus(
            cycle_time  = read_uint16_le(data),
            i2c_errors  = read_uint16_le(data, offset=2),
            sensors     = read_uint16_le(data, offset=4),
            flag        = read_uint32_le(data, offset=6),
            global_conf = read_uint8_le(data, offset=10)
        )
    
    def get_waypoint(self) -> MspWaypoint:
        """Sends the MSP_WP command and gets the data instance."""
        data = self._read_message_data(MSP_WP)

        return MspWaypoint(
            number       = read_uint8_le(data),
            latitude     = read_uint32_le(data, offset=1),
            longitude    = read_uint32_le(data, offset=5),
            alt_hold     = read_uint32_le(data, offset=9),
            heading      = read_uint16_le(data, offset=13),
            time_to_stay = read_uint16_le(data, offset=15),
            flag         = read_uint8_le(data, offset=17)
        )

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

    def set_box(self, data: tuple[BoxItem]) -> NoReturn:
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

    def set_misc(self, data: Misc) -> NoReturn:
        """Sends the MSP_SET_MISC command.

        Sets miscellaneous config parameters on the FC—such as battery voltage scaling, failsafe
        behavior, or other settings not covered by specific MSP commands.
        """
        self._send_message(MSP_SET_MISC, data)

    def set_motor(self, data: MspMotor) -> NoReturn:
        """Sends the MSP_SET_MOTOR command.

        Sets the motor output values on the FC. Motor output values determine the throttle level
        for each motor, controlling the rotation speed and thrust generated by the motors.
        """
        self._send_message(MSP_SET_MOTOR, data)

    def set_pid(self, data: MspPid) -> NoReturn:
        """Sends the MSP_SET_PID command.

        Sets the PID values on the FC. PID values are used to adjust the stability and response
        characteristics of the aircraft.
        """
        self._send_message(MSP_SET_PID, data)

    def set_raw_gps(self, data: MspRawGps) -> NoReturn:
        """Sends the MSP_SET_RAW_GPS command.

        Sets the raw GPS data on the FC—such as the latitude, longitude, altitude, and other
        GPS-related information.
        """
        self._send_message(MSP_SET_RAW_GPS, data)

    def set_raw_rc(self, data: MspRc) -> NoReturn:
        """Sends the MSP_SET_RAW_RC command.

        Sets the raw receiver (RC/RX) channel data on the FC. Raw FC data includes the pulse
        width values received from the transmitter for each channel, typically representing
        control inputs such as throttle, pitch, roll, and yaw.
        """
        self._send_message(MSP_SET_RAW_RC, data)
    
    def set_rc_tuning(self, data: MspRcTuning) -> NoReturn:
        """Sends the MSP_SET_RC_TUNING command.

        Sets RC tuning parameters on the FC—such as expo, rates, and other settings related to
        RC control response and behavior.
        """
        self._send_message(MSP_SET_RC_TUNING, data)

    def set_servo_conf(self, data: tuple[ServoConfItem]) -> NoReturn:
        """Sends the MSP_SET_SERVO_CONF command.

        Sets servo config parameters on the FC—such as servo mapping, direction, endpoints, and
        other settings related to servo control.
        """
        self._send_message(MSP_SET_SERVO_CONF)

    def set_waypoint(self, data: MspWaypoint) -> NoReturn:
        """Sends the MSP_SET_WP command.

        Dispatches a command to set a waypoint on the FC, providing specific latitude, longitude,
        altitude, heading, duration and navigation flags for precise navigation and waypoint
        management.
        """
        self._send_message(MSP_SET_WP, data)

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
