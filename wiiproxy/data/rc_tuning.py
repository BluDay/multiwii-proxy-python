from .  import command_code, struct_format, MultiWiiData
from .. import MSP_RC_TUNING

from typing import NoReturn

@command_code(MSP_RC_TUNING)
@struct_format('7B')
class RcTuning(MultiWiiData):
    """Represents data values for the MSP_RC_TUNING command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _rate: int

    _expo: int

    _roll_pitch_rate: int

    _yaw_rate: int

    _dynamic_throttle_pid: int

    _throttle_mid: int

    _throttle_expo: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._rate                 = None
        self._expo                 = None
        self._roll_pitch_rate      = None
        self._yaw_rate             = None
        self._dynamic_throttle_pid = None
        self._throttle_mid         = None
        self._throttle_expo        = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def rate(self) -> int:
        """Gets the rate value."""
        return self._rate

    @property
    def expo(self) -> int:
        """Gets the expo value."""
        return self._expo

    @property
    def roll_pitch_rate(self) -> int:
        """Gets the roll-pitch rate value."""
        return self._roll_pitch_rate

    @property
    def yaw_rate(self) -> int:
        """Gets the yaw rate value."""
        return self._yaw_rate

    @property
    def dynamic_throttle_pid(self) -> int:
        """Gets the dynamic throttle PID value."""
        return self._dynamic_throttle_pid

    @property
    def throttle_mid(self) -> int:
        """Gets the throttle mid value."""
        return self._throttle_mid

    @property
    def throttle_expo(self) -> int:
        """Gets the throttle expo value."""
        return self._throttle_expo

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
