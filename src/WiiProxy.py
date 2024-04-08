from .multiwii import _MultiWiiDataValues, _MultiWiiMessageHandler

from serial    import Serial
from threading import Thread
from time      import sleep
from queue     import PriorityQueue

class WiiProxy(object):
    """
    The main class of this module that handles everything.
    
    This class merely requires an open serial connection—at baudrate 115200—to be passed at
    instantiation. Everything else, like the commands, the thread, each data instance, gets
    created automatically.

    This module only supports MSP v1 and not any of the newer versions.
    """

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """
    Default maximum size for the priority queue.
    """
    _DEFAULT_QUEUE_MAXSIZE: int = 100

    """
    Default delay (in seconds) for serial writes.
    """
    _DEFAULT_WRITE_DELAY: float = 0.005

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

        self._command_queue = PriorityQueue(maxsize=self._DEFAULT_QUEUE_SIZE)

        self._data = _MultiWiiDataValues()

        self._is_active = False

        self._serial = serial

        self._thread = Thread(target=self._handle_command_queue)

        self._write_delay = self._DEFAULT_WRITE_DELAY

        self._data.reset_data()

    def __del__(self) -> None:
        """
        Stops the worker and the thread at destruction.
        """
        self.stop()

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def data(self) -> _MultiWiiDataValues:
        """
        Gets the MultiWii data values instance.

        Returns:
            _MultiWiiDataValues: The data values instance.
        """
        return self._data

    @property
    def is_active(self) -> bool:
        """
        Gets a value indicating whether the module is communicating to the flight controller.
        """
        return self._is_active

    @property
    def write_delay(self) -> float:
        """
        Gets the number of seconds to delay each write operation with in seconds.

        Returns:
            float: The delay value as a floating-point.
        """
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

    # ------------------------------------ INSTANCE METHODS ------------------------------------
    
    def _handle_command_queue(self) -> None:
        """The thread worker method that performs the whole communication part.

        This worker method runs continously in a thread and handles everything
        from enqueuing commands and sending messages to the flight controller, to
        receiving messages and updating their corresponding data value instances.
        """
        while True:
            # TODO: Fill command queue with prioritized commands if empty.
            # TODO: Dequeue the most prioritized command from the queue.
            # TODO: Reset the input/output buffer.
            # TODO: Send message with empty data values to receive a response.
            # TODO: Read response message.
            # TODO: Update corresponding instance for command with new values if not null.
            # TODO: Indicate that the command has been processed.

            pass

    # TODO: Get size and format for command.
    # TODO: Create payload tuple.
    # TODO: Assembly message using the format and payload.
    # TODO: Write message to the serial port.
    # TODO: Sleep for `write_delay` seconds.

    # TODO: Read preamble, code and data size.
    # TODO: Validate preamble.
    # TODO: Read data value bytes and checksum value.
    # TODO: Unpack the whole message.
    # TODO: Return the unpacked message.

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
