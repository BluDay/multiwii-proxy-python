from serial    import Serial
from struct    import pack, unpack
from threading import Thread
from time      import sleep
from queue     import PriorityQueue

class WiiProxy(object):
    """The main class of this module that handles everything.
    
    This class merely requires an open serial connection---at baudrate 115200---to be
    passed at instantiation. Everything else, like the commands, the thread, each data
    instance, gets created automatically.

    This module and this class only supports the legacy version of MSP (MultiWii Serial Protocol).
    """

    """The base format string for the message preamble."""
    __MESSAGE_PREAMBLE_BASE_FORMAT = '$M'

    """The message direction characters."""
    __MESSAGE_DIRECTION_INCOMING_CHAR = '<'
    __MESSAGE_DIRECTION_OUTGOING_CHAR = '>'

    """ATmega328 microprocessor and most Arduino-based microcontrollers use Little-endian."""
    _ENDIANNESS = '<' # '>'

    """Same as above, but for serializing `int`s without `struct`."""
    _INT_BYTEORDER = 'little'

    """The message preamble format for `struct.pack` and `struct.unpack`."""
    _PREAMBLE_STRUCT_FORMAT = f'{ENDIANNESS}3b'

    """Same as above, but for the payload.

    The format consists of a `%s` specifier and is used for creating complete payload
    formats using either a dynamic or a non-dynamic data format for a specific command.
    """
    _PAYLOAD_STRUCT_FORMAT = f'{ENDIANNESS}2B'

    """
    A pre-packed preamble payload for incoming messages. All message preambles for
    incoming messages are the same, and do not need to be re-packed every single
    time at runtime.

    Example:

        \\x24\\x4d\\x3c

        $M< (ASCII)
    """
    _PREAMBLE_IN = pack(_PREAMBLE_STRUCT_FORMAT, '$M<')

    """
    Same as above, but with outgoing messages.

    Example:

        \\x24\\x4d\\x3e

        $M> (ASCII)
    """
    _PREAMBLE_OUT = pack(_PREAMBLE_STRUCT_FORMAT, '$M>')

    def __init__(self, serial: Serial) -> None:
        """Initializes an instance using the provided serial connection.
        
        The provided serial instance that presumably has been connected with a device
        with a baudrate of 115200.


        Parameters:
            serial (Serial): The serial connection instance.
        """
        self._is_active = False

        self._data = {
            MultiWiiCommands.IDENT:      Ident(),
            MultiWiiCommands.STATUS:     Status(),
            MultiWiiCommands.RAW_IMU:    RawImu(),
            MultiWiiCommands.SERVO:      Servo(),
            MultiWiiCommands.SERVO_CONF: ServoConf(),
            MultiWiiCommands.MOTOR:      Motor(),
            MultiWiiCommands.MOTOR_PINS: MotorPins(),
            MultiWiiCommands.RC:         Rc(),
            MultiWiiCommands.RC_TUNING:  RcTuning(),
            MultiWiiCommands.ATTITUDE:   Attitude(),
            MultiWiiCommands.ALTITUDE:   Altitude(),
            MultiWiiCommands.RAW_GPS:    RawGps(),
            MultiWiiCommands.COMP_GPS:   CompGps(),
            MultiWiiCommands.WP:         Waypoint(),
            MultiWiiCommands.ANALOG:     Analog(),
            MultiWiiCommands.PID:        Pid(),
            MultiWiiCommands.PIDNAMES:   PidNames(),
            MultiWiiCommands.BOX:        Box(),
            MultiWiiCommands.BOXNAMES:   BoxNames(),
            MultiWiiCommands.BOXIDS:     BoxIds(),
            MultiWiiCommands.MISC:       Misc()
        }

        self._command_queue = PriorityQueue(100)

        self._serial = serial

        self._thread = Thread(target=self._handle_command_queue)

        self._write_delay = 0.005

    def __del__(self) -> None:
        """None: Stops the worker and the thread at destruction."""
        self._stop()

    @property
    def is_active(self) -> bool:
        """bool: Gets a value indicating whether the module is communicating to the flight controller."""
        return self._is_active

    @property
    def data(self) -> dict:
        """dict: Gets the command-to-data instance map for accessing read and processed values."""
        return self._data

    @property
    def write_delay(self) -> float:
        """float: Gets the delay value for serial writes."""
        return self._write_delay

    @write_delay.setter
    def write_delay(self, value: float) -> None:
        """Sets the write delay value.

        Parameters:
            value (float): A floating-point value in seconds.
        """
        if not isinstance(value, float):
            raise TypeError

        if value < 0:
            raise ValueError
            
        self._write_delay = value
    
    @classmethod
    def __assemble_message(cls, format: str, data: tuple) -> bytes:
        """Assembles a complete serialized message with the provided format and data values.

        Parameters:
            format (str): The payload struct format.
            data (tuple): The data values.

        Returns:
            bytes: an array of bytes for the whole message.
        """
        payload = pack(format, *data)
            
        checksum = cls.__get_crc(payload).to_bytes(
            length=1,
            byteorder=cls._INT_BYTEORDER,
            signed=False
        )

        return cls._PREAMBLE_IN + payload + checksum

    @classmethod
    def __disassemble_message(cls, format: str, payload: bytes) -> tuple:
        """Disassembles a serialized outgoing message into a tuple of raw values.

        Parameters:
            format (str): A `struct` format for the full message.
            payload (bytes): The full message buffer.

        Returns:
            tuple: A tuple of raw and unevaluated values of integers.
        """
        return unpack(format, payload)
    
    @classmethod
    def get_message_preamble_base_format_string(cls, incoming: bool) -> str:
        """Gets the message preamble, including the message direction character.

        Parameters:
            incoming (bool): Decides which direction characters should be included.

        Returns:
            str: A preamble format string with a direction char.

        Example:
            incoming = True  -> "$M<"
            incoming = False -> "$M>"
        """
        if incoming:
            direction = cls.__MESSAGE_DIRECTION_INCOMING_CHAR
        else:
            direction = cls.__MESSAGE_DIRECTION_OUTGOING_CHAR

        return cls.__MESSAGE_PREAMBLE_BASE_FORMAT + direction

    @staticmethod
    def __get_crc(payload: bytes) -> int:
        """Calculates the a single byte checksum using CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): A serialized payload buffer.

        Returns:
            int: The calculated CRC value for the provided payload.
        """
        checksum = 0

        for value in payload: checksum ^= value

        return checksum

    @staticmethod
    def __get_dynamically_sized_data_format(format: str, size: int) -> str:
        """Why did I do this?

        Parameters:
            format (str): The `struct` format for the data values.
            size (int): The size or length of the data values in the full payload.

        Returns:
            str: The `struct` format for the required data values.
        """
        if len(format) > 2:
            return format * size

        return f'{str(size)}{format}'

    def __handle_command_queue(self) -> None:
        """The thread worker method that performs the whole communication part.

        This worker method runs continously in a thread and handles everything
        from enqueuing commands and sending messages to the flight controller,
        to receiving messages and updating their corresponding data value instance
        in the `self._data` dictionary.

        Control flow: 

            1. Create prioritized commands if the queue is empty and enqueue them.
            2. Dequeue one command per iteration.
            3. Flush the input/output buffer of the serial device.
            4. Send and construct a message using the dequeued command with empty values.
            5. Read the output buffer for an outgoing message.
            6. Update the corresponding the values of the corresponding data value
               instance using the received data values if not null---skip to the next
               iteration if null.
            7. Signal that the dequeued task has been completed.
        """
        while self._is_active:
            if self._command_queue.empty():
                for command in self._data:
                    prioritized_command = (command.priority, command)

                    self._command_queue.put(prioritized_command)

            command = self._command_queue.get()

            self.__flush_serial_io_buffer()

            self.__send_message(command, data=())

            data = self.__read_message(command)

            if data is None: continue

            self._data[command].update_values(data)

            self._command_queue.task_done()

    def __send_message(self, command: Command, data: tuple) -> None:
        """Creates a serialized message and sends it to the flight controller.

        Parameters:
            command (Command): The command to execute on the FC.
            data (tuple): A tuple of raw integer values to sent to the FC.
        """
        size   = command.size
        format = command.format

        if not data:
            size   = 0
            format = ''
        elif command.is_dynamic:
            size   = size ** 2
            format = self.__get_dynamically_sized_data_format(format, size)

        payload = (size, command.code, *data)

        buffer = self.__assemble_message(format, payload)

        self._serial.write(buffer)

        sleep(self._write_delay)

    def _read_message(self, command: Command) -> tuple:
        """Attempts to read a message of a specific command from the serial connection.

        Parameters:
            command (Command): The targeted command.

        Returns:
            tuple: An immutable list of data values for the command.
        """
        buffer = self._serial.read(3)

        if buffer[2] is not cls._OUT:
            return None

        buffer += self._serial.read(2)

        if buffer[4] != command.code:
            return None

        data_size = buffer[3]

        buffer += self._serial.read(data_size + 1)

        payload = buffer[3:-1]

        checksum = buffer[-1]

        if checksum != self.__get_crc(payload):
            return None

        format = None

        if command.is_dynamic:
            format = self.__get_dynamically_sized_data_format(
                format=command.format,
                size=data_size // command.size
            )
        else:
            format = command.format

        message = self.__disassemble_message(format, buffer)

        if message is not None: return None

        return message[5:-1]

    def _flush_serial_io_buffer(self) -> None:
        """Flushes both the input and output buffer of the serial connection."""
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

    def start(self) -> None:
        """Starts the worker thread and enables communication to the craft."""
        if self._is_active: return
        
        self._thread.start()
        
        self._is_active = True

    def stop(self) -> None:
        """"Stops the worker thread and disables communication to the craft."""
        if not self._is_active: return

        self._thread.join()

        self._is_active = False
