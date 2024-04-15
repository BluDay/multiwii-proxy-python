from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.MISC)
@MultiWiiDataStructure.struct_format('6HIH4B')
class Misc(MultiWiiDataStructure):
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
