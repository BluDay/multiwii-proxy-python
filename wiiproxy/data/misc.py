from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

@command_code(MspCommands.MISC)
@struct_format('6HIH4B')
class Misc(MultiWiiData):
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
