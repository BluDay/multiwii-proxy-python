from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_PID

from typing import NamedTuple

@command_code(MSP_PID)
@struct_format('30B')
class MspPid(_MspValues):
    """Represents data values for the MSP_PID command."""
    pass

class MspSetPid(NamedTuple):
    """Represents data values for the MSP_SET_PID command."""
    roll_p: int
    roll_i: int
    roll_d: int

    pitch_p: int
    pitch_i: int
    pitch_d: int

    yaw_p: int
    yaw_i: int
    yaw_d: int

    alt_p: int
    alt_i: int
    alt_d: int

    pos_p: int
    pos_i: int
    pos_d: int

    posr_p: int
    posr_i: int
    posr_d: int

    navr_p: int
    navr_i: int
    navr_d: int

    level_p: int
    level_i: int
    level_d: int

    mag_p: int
    mag_i: int
    mag_d: int

    vel_p: int
    vel_i: int
    vel_d: int
