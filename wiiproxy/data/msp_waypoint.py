from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_WP

from typing import NamedTuple, Self

@command_code(MSP_WP)
@struct_format('B3I2HB')
class MspWaypoint(_MspDataStructure):
    """Represents data values for the MSP_WP command."""
    number: int

    latitude: int

    longitude: int

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int

    @staticmethod
    def parse(self, data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspWaypoint(**data)

class MspSetWaypoint(NamedTuple):
    """Represents data values for the MSP_SET_WP command."""
    number: int

    latitude: int

    longitude: int

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
