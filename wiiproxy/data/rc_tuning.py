from ._base import MultiWiiDataStructure

class RcTuning(MultiWiiDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""

    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int
