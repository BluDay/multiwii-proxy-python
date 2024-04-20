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
    
    This class merely requires an open serial port—with a baudrate of 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default maximum size for the priority queue."""
    DEFAULT_COMMAND_QUEUE_MAXSIZE: Final[int] = 100

    """Default delay (in seconds) for serial writes."""
    DEFAULT_COMMAND_WRITE_DELAY: Final[float] = 0.005

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _is_active: bool

    _command_processing_thread: Thread

    _command_queue: PriorityQueue 

    _command_write_delay: int

    _serial: Serial

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial port."""
        self._is_active = False

        if not isinstance(serial, Serial):
            raise TypeError('Argument "serial" must be an instance of "serial.Serial".')

        super().__init__()

        self._command_processing_thread = Thread(target=self._process_command_queue)

        self._command_queue = PriorityQueue(maxsize=MultiWii.DEFAULT_COMMAND_QUEUE_MAXSIZE)

        self._command_write_delay = MultiWii.DEFAULT_COMMAND_WRITE_DELAY

        self._serial = serial

    def __del__(self) -> NoReturn:
        """Stops the worker and thread upon destruction.

        This destructor stops the worker thread and cleans up resources before the instance
        is destroyed.
        """
        self.stop()

        self._serial = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def is_active(self) -> bool:
        """Gets a value indicating whether the flight controller communication is active."""
        return self._is_active

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
        """Sets the write delay value."""
        if not isinstance(value, float):
            raise TypeError('Value must be a float.')

        if value < 0:
            raise ValueError('Value must be a non-negative number.')
            
        self._command_write_delay = value

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _clear_command_queue(self) -> NoReturn:
        """Clears the command queue completely.

        This method empties the command queue by removing all pending commands.
        """
        while not self._command_processing_queue.empty():
            try:
                self._command_processing_queue.get(block=False)
            except QueueEmpty:
                continue

            self._command_processing_queue.task_done()

    def _fill_command_queue(self) -> NoReturn:
        """Fills the command queue with prioritized commands if empty.

        This method checks if the command queue is empty and fills it with prioritized
        commands if necessary. Prioritized commands are added to ensure that higher-priority
        commands are processed first.
        """
        pass

    def _process_command_queue(self) -> NoReturn:
        """Worker method responsible for managing communication with the flight controller.

        This method continously processes commands queued for execution, handling the entire
        communication process with the flight controller. It runs continously in a thread,
        ensuring that commands are enqueued, sent, and processed efficiently.

        Control Flow
        ------------
        1. Fill the command queue with prioritized commands if it is empty.
        2. Dequeue the most prioritized command from the queue.
        3. Reset the input and output buffers of the serial port for clean communication.
        3. Send the command with empty data values to receive a response.
        4. Read the response command with received data values.
        5. Update the corresponding instance for the command with new values.
        6. Indicate that the command has been processed.
        
        Note
        ----
        - Commands should be properly enqueued into the command queue before invoking this
          method.
        - Each command should be prioritized based on its importance or urgency for proper
          processing.
        """
        while self._is_active:
            self._fill_command_queue()

            self._process_commands()

            sleep(0.1)

    def _process_command(self, command: int, data: tuple) -> NoReturn:
        """Processes the provided command.

        This method send the provided command with associated data to the flight controller
        and handles the response, if any. It updates corresponding data values based on the
        received response.
        """
        pass

    def _process_commands(self) -> NoReturn:
        """Processes all enqueued commands.

        This method dequeues and processes all commands currently in the command queue.
        For each command, it calls the _process_command method to send the command to the
        flight controller, reads the response, and updates the corresponding data values
        if new values have been receieved.
        """
        pass

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

    def start(self) -> NoReturn:
        """Starts the communication thread.
        
        This method starts the communication thread responsible for processing commands.
        If the thread is already active, this method returns immediately without taking
        any action.

        Raises
        ------
        RuntimeError
            If the thread has already been started.

        Any other exceptions raised during the start operation are logged.
        """
        if self._is_active: return
        
        try:
            self._command_processing_thread.start()

            self._is_active = True
        except RuntimeError as e:
            print(f'Communication thread has already been started: {e}')
        except Exception as e:
            print(f'Exception occured while starting the communication thread: {e}')

    def stop(self) -> NoReturn:
        """Stops the communication thread.

        This method stops the communication thread and performs necessary cleanup tasks.
        If the thread is not active, this method returns immediately without taking any
        action.

        Raises
        ------
        RuntimeError
            If the thread has not been started.

        Any other exceptions raised during the join operation or command queue clearance
        are logged.
        """
        if not self._is_active: return

        try:
            self._command_processing_thread.join()

            self._clear_command_queue()

            self._is_active = False
        except RuntimeError as e:
            print(f'Communication thread has not been started: {e}')
        except Exception as e:
            print(f'Exception occured while stopping the communication thread: {e}')
