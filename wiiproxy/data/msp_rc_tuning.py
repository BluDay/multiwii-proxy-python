from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_RC_TUNING

from typing import NoReturn

@command_code(MSP_RC_TUNING)
@struct_format('7B')
class MspRcTuning(_MultiWiiData):
    """Represents data values for the MSP_RC_TUNING command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __rate: int

    __expo: int

    __roll_pitch_rate: int

    __yaw_rate: int

    __dynamic_throttle_pid: int

    __throttle_mid: int

    __throttle_expo: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__rate                 = None
        self.__expo                 = None
        self.__roll_pitch_rate      = None
        self.__yaw_rate             = None
        self.__dynamic_throttle_pid = None
        self.__throttle_mid         = None
        self.__throttle_expo        = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def rate(self) -> int:
        """Gets the rate value."""
        return self.__rate

    @property
    def expo(self) -> int:
        """Gets the expo value."""
        return self.__expo

    @property
    def roll_pitch_rate(self) -> int:
        """Gets the roll-pitch rate value."""
        return self.__roll_pitch_rate

    @property
    def yaw_rate(self) -> int:
        """Gets the yaw rate value."""
        return self.__yaw_rate

    @property
    def dynamic_throttle_pid(self) -> int:
        """Gets the dynamic throttle PID value."""
        return self.__dynamic_throttle_pid

    @property
    def throttle_mid(self) -> int:
        """Gets the throttle mid value."""
        return self.__throttle_mid

    @property
    def throttle_expo(self) -> int:
        """Gets the throttle expo value."""
        return self.__throttle_expo

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
