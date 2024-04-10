from .data.base.MultiWiiDataValues import MultiWiiDataValues

from serial    import Serial
from threading import Thread
from time      import sleep
from typing    import ClassVar, Final
from queue     import PriorityQueue

class MultiWii(object, MultiWiiDataValues):
    """
    The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial connection—at baudrate 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

    _command_queue: ClassVar[PriorityQueue]

    _thread: ClassVar[Thread]

    is_active: ClassVar[bool]

    serial: ClassVar[Serial]

    write_delay: ClassVar[int]

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """
    Default maximum size for the priority queue.
    """
    DEFAULT_QUEUE_MAXSIZE: Final[int] = 100

    """
    Default delay (in seconds) for serial writes.
    """
    DEFAULT_WRITE_DELAY: Final[float] = 0.005

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> None:
        """
        Initializes an instance using the provided serial connection.
        
        The provided serial instance that presumably has been connected with a device
        with a baudrate of 115200.

        Parameters:
            serial (Serial): The serial connection instance.
        """
        if not isinstance(serial, Serial):
            raise TypeError

        self._command_queue = PriorityQueue(maxsize=self.DEFAULT_QUEUE_SIZE)

        self._thread = Thread(target=self._handle_command_queue)

        self.is_active = False

        self.serial = serial

        self.write_delay = self.DEFAULT_WRITE_DELAY

        self._reset_data()

    def __del__(self) -> None:
        """
        Stops the worker and the thread at destruction.
        """
        self.stop()

        self._command_queue = None

        self._thread = None

        self.serial = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @write_delay.setter
    def write_delay(self, value: float) -> None:
        """
        Sets the write delay value.

        Parameters:
            value (float): A floating-point value in seconds.
        """
        if not isinstance(value, float):
            raise TypeError

        if value < 0:
            raise ValueError
            
        self.write_delay = value

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def _calculate_crc(payload: bytes) -> int:
        """
        Calculates the checksum for the payload using an XOR CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): The serialized payload.

        Returns:
            int: The calculated checksum value.
        """
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum

    # ------------------------------------ INSTANCE METHODS ------------------------------------
    
    def _handle_command_queue(self) -> None:
        """
        The thread worker method that performs the whole communication part.

        This worker method runs continously in a thread and handles everything
        from enqueuing commands and sending messages to the flight controller, to
        receiving messages and updating their corresponding data value instances.

        Control flow for each while iteration:

            1. Fill command queue with prioritized commands if empty.
            2. Dequeue the most prioritized command from the queue.
            3. Reset the input/output buffer.
            3. Send message with empty data values to receive a response.
            4. Read response message.
            5. Update corresponding instance for command with new values if not null.
            6. Indicate that the command has been processed.
        """
        while True:
            pass

    def _reset_input_output_buffer(self) -> None:
        """
        Resets both the input and output buffer of the serial connection.
        """
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

    def start(self) -> None:
        """
        Starts the worker thread and enables communication to the craft.
        """
        if self._is_active:
            return
        
        self._thread.start()
        
        self._is_active = True

    def stop(self) -> None:
        """
        Stops the worker thread and disables all communication.
        """
        if not self._is_active:
            return

        self._thread.join()

        self._is_active = False
