from . import _MspDataStructure, _Point2D, command_code, struct_format

from ..msp_commands import MSP_RAW_GPS

from typing import NamedTuple, Self

@command_code(MSP_RAW_GPS)
@struct_format('2B2I3H')
class MspRawGps(_MspDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: int

    satellites: int

    latitude: int

    longitude: int

    altitude: int

    speed: int

    ground_course: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspRawGps(
            data[0],
            data[1],
            data[2] / 10000000,
            data[3] / 10000000,
            data[4],
            data[5] * 10
        )

def MspSetRawGps(NamedTuple):
    """Represents data values for the MSP_SET_RAW_GPS command."""
    fix: int

    satellites: int

    latitude: int

    longitude: int

    altitude: int

    speed: int

    ground_course: int
