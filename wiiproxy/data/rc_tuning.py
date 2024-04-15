from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.RC_TUNING)
@MultiWiiDataStructure.struct_format('7B')
class RcTuning(MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""

    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int
