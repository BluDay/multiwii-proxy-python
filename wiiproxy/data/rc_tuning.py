from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

@command_code(MspCommands.RC_TUNING)
@struct_format('7B')
class RcTuning(MultiWiiData):
    """Represents data values for the MSP_RC_TUNING command."""

    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int
