from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_COMP_GPS

from typing import Self

@command_code(MSP_COMP_GPS)
@struct_format('2HB')
class MspCompGps(_MspDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: int

    direction_to_home: int

    update: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspCompGps(data[0], data[1], data[2])
