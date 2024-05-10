from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_RC_TUNING

from typing import NamedTuple, Self

@command_code(MSP_RC_TUNING)
@struct_format('7B')
class MspRcTuning(_MspDataStructure):
    """Represents data values for the MSP_RC_TUNING command."""
    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspRcTuning(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6]
        )

class MspSetRcTuning(NamedTuple):
    """Represents data values for the MSP_SET_RC_TUNING command."""
    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int
