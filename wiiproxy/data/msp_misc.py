from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_MISC

from typing import NoReturn

@command_code(MSP_MISC)
@struct_format('6HIH4B')
class MspMisc(_MultiWiiData):
    """Represents data values for the MSP_MISC command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __power_trigger: int

    __throttle_failsafe: int

    __throttle_idle: int

    __throttle_min: int

    __throttle_max: int

    __plog_arm: int

    __plog_lifetime: int

    __mag_declination: int

    __battery_scale: int

    __battery_warn_1: int

    __battery_warn_2: int

    __battery_critical: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__power_trigger     = None
        self.__throttle_failsafe = None
        self.__throttle_idle     = None
        self.__throttle_min      = None
        self.__throttle_max      = None
        self.__plog_arm          = None
        self.__plog_lifetime     = None
        self.__mag_declination   = None
        self.__battery_scale     = None
        self.__battery_warn_1    = None
        self.__battery_warn_2    = None
        self.__battery_critical  = None

    # --------------------------------------- PROPERTIES ---------------------------------------

    @property
    def power_trigger(self) -> int:
        """Gets the power trigger value."""
        return self.__power_trigger

    @property
    def throttle_failsafe(self) -> int:
        """Gets the throttle failsafe value."""
        return self.__throttle_failsafe

    @property
    def throttle_idle(self) -> int:
        """Gets the throttle idle value."""
        return self.__throttle_idle

    @property
    def throttle_min(self) -> int:
        """Gets the minimum throttle value."""
        return self.__throttle_min

    @property
    def throttle_max(self) -> int:
        """Gets the maximum throttle value."""
        return self.__throttle_max

    @property
    def plog_arm(self) -> int:
        """Gets the plog arm value."""
        return self.__plog_arm

    @property
    def plog_lifetime(self) -> int:
        """Gets the plog lifetime value."""
        return self.__plog_lifetime

    @property
    def mag_declination(self) -> int:
        """Gets the mag declination value."""
        return self.__mag_declination

    @property
    def battery_scale(self) -> int:
        """Gets the battery scale value."""
        return self.__battery_scale

    @property
    def battery_warn_1(self) -> int:
        """Gets the first battery warning value."""
        return self.__battery_warn_1

    @property
    def battery_warn_2(self) -> int:
        """Gets the second battery warning value."""
        return self.__battery_warn_2

    @property
    def battery_critical(self) -> int:
        """Gets the critical battery value."""
        return self.__battery_critical

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
