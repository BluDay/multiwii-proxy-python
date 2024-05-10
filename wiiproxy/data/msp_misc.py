from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_MISC

from typing import NamedTuple, Self

@command_code(MSP_MISC)
@struct_format('6HIH4B')
class MspMisc(_MspDataStructure):
    """Represents data values for the MSP_MISC command."""
    power_trigger: int

    throttle_failsafe: int

    throttle_idle: int

    throttle_min: int

    throttle_max: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: int

    battery_scale: int

    battery_warn_1: int

    battery_warn_2: int

    battery_critical: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspMisc(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7] / 10,
            data[8],
            data[9] / 10,
            data[10] / 10,
            data[11] / 10
        )

class MspSetMisc(NamedTuple):
    """Represents data values for the MSP_MISC command."""
    power_trigger: int

    throttle_min: int

    throttle_max: int

    min_command: int

    failsafe_throttle: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: int

    battery_scale: int

    battery_warn_1: int

    battery_warn_2: int

    battery_critical: int
