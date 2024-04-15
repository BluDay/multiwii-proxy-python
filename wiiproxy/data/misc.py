from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(114)
@msp_data_struct_format('6HIH4B')
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
