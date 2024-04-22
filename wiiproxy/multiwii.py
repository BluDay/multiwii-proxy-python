from . import MultiWiiBase

from serial import Serial
from time   import sleep
from typing import Final, NoReturn

class MultiWii(MultiWiiBase):
    """The main class for wiiproxy that handles everything.
    
    This class merely requires an open serial port—with a baudrate of 115200—to be passed at
    instantiation. Everything else—like the commands, the thread, each data instance—gets
    created automatically.

    Supports MSP v1 and not any of the newer versions.
    """
    
    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """Default delay (in seconds) for serial writes."""
    DEFAULT_COMMAND_WRITE_DELAY: Final[float] = 0.005

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _command_write_delay: int

    _serial: Serial

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self, serial: Serial) -> NoReturn:
        """Initializes an instance using the provided serial port."""
        self._is_active = False

        if not isinstance(serial, Serial):
            raise TypeError('Argument "serial" must be an instance of "serial.Serial".')

        super().__init__()

        self._serial = serial

    # --------------------------------------- PROPERTIES ---------------------------------------

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
