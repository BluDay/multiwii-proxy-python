from . import MultiWiiBase

from serial    import Serial
from threading import Thread
from time      import sleep
from typing    import Final, NoReturn

from queue import (
    Empty as QueueEmpty,
    Full  as QueueFull,
    PriorityQueue
)

class MultiWii(MultiWiiBase):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial connection—at baudrate 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default maximum size for the priority queue."""
    DEFAULT_MESSAGE_QUEUE_MAXSIZE: Final[int] = 100

    """Default delay (in seconds) for serial writes."""
    DEFAULT_MESSAGE_WRITE_DELAY: Final[float] = 0.005

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _is_active: bool

    _message_processing_thread: Thread

    _message_queue: PriorityQueue 

    _message_write_delay: int

    _serial: Serial

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial connection.
        
        The provided serial instance that presumably has been connected with a device
        with a baudrate of 115200.

        Parameters:
            serial (Serial): The serial connection instance.
        """
        self._is_active = False

        if not isinstance(serial, Serial):
            raise TypeError

        super().__init__()

        self._message_processing_thread = Thread(target=self._process_message_queue)

        self._message_queue = PriorityQueue(maxsize=MultiWii.DEFAULT_MESSAGE_QUEUE_MAXSIZE)

        self._message_write_delay = MultiWii.DEFAULT_MESSAGE_WRITE_DELAY

        self._serial = serial

    def __del__(self) -> NoReturn:
        """Stops the worker and the thread at destruction."""
        self.stop()

        self._serial = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def is_active(self) -> bool:
        """Gets a value indicating whether the flight controller communication is active."""
        return self._is_active

    @property
    def message_write_delay(self) -> float:
        """Gets the message write delay."""
        return self._message_write_delay

    @property
    def serial(self) -> Serial:
        """Gets the used serial instance that was provided at instantiation."""
        return self._serial

    @message_write_delay.setter
    def message_write_delay(self, value: float) -> NoReturn:
        """Sets the write delay value.

        Parameters:
            value (float): A floating-point value in seconds.
        """
        if not isinstance(value, float):
            raise TypeError

        if value < 0:
            raise ValueError('Must be a positive number.')
            
        self._message_write_delay = value

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _clear_message_queue(self) -> NoReturn:
        """Clears the message queue completely."""
        while not self._message_processing_queue.empty():
            try:
                self._message_processing_queue.get(block=False)
            except QueueEmpty:
                continue

            self._message_processing_queue.task_done()

    def _fill_message_queue(self) -> NoReturn:
        """Fill the message queue with commands of a non-inactive priority value."""
        pass

    def _process_message_queue(self) -> NoReturn:
        """The thread worker method that performs the whole communication part.

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
        while self._is_active:
            pass

    def _reset_serial_io_buffers(self) -> NoReturn:
        """Resets both the input and output buffer of the serial connection."""
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

    def start(self) -> NoReturn:
        """Starts the worker thread and enables communication to the craft."""
        if self._is_active: return
        
        self._message_processing_thread.start()
        
        self._is_active = True

    def stop(self) -> NoReturn:
        """Stops the worker thread and disables all communication."""
        if not self._is_active: return

        self._message_processing_thread.join()

        self._clear_message_queue()

        self._is_active = False
