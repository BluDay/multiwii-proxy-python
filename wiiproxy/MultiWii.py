from wiiproxy.data.base.MultiWiiDataValues import MultiWiiDataValues

from serial    import Serial
from threading import Thread
from time      import sleep
from typing    import ClassVar, Final, NoReturn
from queue     import PriorityQueue

class MultiWii(object, MultiWiiDataValues):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial connection—at baudrate 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

    _is_active: ClassVar[bool]

    _message_processing_thread: ClassVar[Thread | None]

    _message_queue: ClassVar[PriorityQueue | None]

    _message_write_delay: ClassVar[int]

    _serial: ClassVar[Serial | None]

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default maximum size for the priority queue."""
    DEFAULT_MESSAGE_QUEUE_MAXSIZE: Final[int] = 100

    """Default delay (in seconds) for serial writes."""
    DEFAULT_WRITE_DELAY: Final[float] = 0.005

    """The MSP version used."""
    MSP_VERSION: Final[str] = 'v1'

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial connection.
        
        The provided serial instance that presumably has been connected with a device
        with a baudrate of 115200.

        Parameters:
            serial (Serial): The serial connection instance.
        """
        if not isinstance(serial, Serial):
            raise TypeError

        self._is_active = False

        self._message_processing_thread = Thread(target=self._process_message_queue)

        self._message_queue = PriorityQueue(maxsize=self.DEFAULT_MESSAGE_QUEUE_MAXSIZE)

        self._message_write_delay = self.DEFAULT_WRITE_DELAY

        self._serial = serial

        self._reset_data()

    def __del__(self) -> NoReturn:
        """Stops the worker and the thread at destruction."""
        self.stop()

        self._message_processing_thread = None

        self._message_queue = None

        self._serial = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def is_active(self) -> bool:
        """Gets a value indicating whether the flight controller communication is active."""
        return self._is_active

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
            raise ValueError
            
        self._message_write_delay = value

    # ------------------------------------ INSTANCE METHODS ------------------------------------
    
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
        while True:
            pass

    def _reset_input_output_buffer(self) -> NoReturn:
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

        self._is_active = False
