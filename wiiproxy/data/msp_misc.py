from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_MISC

from typing import NoReturn

@command_code(MSP_MISC)
@struct_format('6HIH4B')
class MspMisc(_MspDataStructure):
    """Represents data values for the MSP_MISC command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _power_trigger: int

    _throttle_failsafe: int

    _throttle_idle: int

    _throttle_min: int

    _throttle_max: int

    _plog_arm: int

    _plog_lifetime: int

    _mag_declination: int

    _battery_scale: int

    _battery_warn_1: int

    _battery_warn_2: int

    _battery_critical: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._power_trigger     = None
        self._throttle_failsafe = None
        self._throttle_idle     = None
        self._throttle_min      = None
        self._throttle_max      = None
        self._plog_arm          = None
        self._plog_lifetime     = None
        self._mag_declination   = None
        self._battery_scale     = None
        self._battery_warn_1    = None
        self._battery_warn_2    = None
        self._battery_critical  = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def power_trigger(self) -> int:
        """Gets the power trigger value."""
        return self._power_trigger

    @property
    def throttle_failsafe(self) -> int:
        """Gets the throttle failsafe value."""
        return self._throttle_failsafe

    @property
    def throttle_idle(self) -> int:
        """Gets the throttle idle value."""
        return self._throttle_idle

    @property
    def throttle_min(self) -> int:
        """Gets the minimum throttle value."""
        return self._throttle_min

    @property
    def throttle_max(self) -> int:
        """Gets the maximum throttle value."""
        return self._throttle_max

    @property
    def plog_arm(self) -> int:
        """Gets the plog arm value."""
        return self._plog_arm

    @property
    def plog_lifetime(self) -> int:
        """Gets the plog lifetime value."""
        return self._plog_lifetime

    @property
    def mag_declination(self) -> int:
        """Gets the mag declination value."""
        return self._mag_declination

    @property
    def battery_scale(self) -> int:
        """Gets the battery scale value."""
        return self._battery_scale

    @property
    def battery_warn_1(self) -> int:
        """Gets the first battery warning value."""
        return self._battery_warn_1

    @property
    def battery_warn_2(self) -> int:
        """Gets the second battery warning value."""
        return self._battery_warn_2

    @property
    def battery_critical(self) -> int:
        """Gets the critical battery value."""
        return self._battery_critical

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._power_trigger     = data[0]
        self._throttle_failsafe = data[1]
        self._throttle_idle     = data[2]
        self._throttle_min      = data[3]
        self._throttle_max      = data[4]
        self._plog_arm          = data[5]
        self._plog_lifetime     = data[6]
        self._mag_declination   = data[7] / 10
        self._battery_scale     = data[8]
        self._battery_warn_1    = data[9] / 10
        self._battery_warn_2    = data[10] / 10
        self._battery_critical  = data[11] / 10
