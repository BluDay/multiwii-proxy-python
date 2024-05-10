from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_ALTITUDE

from typing import Self

@command_code(MSP_ALTITUDE)
@struct_format('ih')
class MspAltitude(_MspDataStructure):
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: int

    pressure_variation: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspAltitude(data[0], data[1])
