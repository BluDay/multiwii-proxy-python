from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.RC_TUNING)
@msp_data_struct_format('7B')
class RcTuning(MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""

    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int
