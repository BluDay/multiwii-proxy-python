from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_RC

from typing import NamedTuple, Self

@command_code(MSP_RC)
@struct_format('8H')
class MspRc(_MspDataStructure):
    """Represents data values for the MSP_RC command."""
    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspRc(data[0], data[1], data[2], data[3], data[4:])

class MspSetRawRc(NamedTuple):
    """Represents data values for the MSP_SET_RAW_RC command."""
    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux1: int

    aux2: int

    aux3: int

    aux4: int
