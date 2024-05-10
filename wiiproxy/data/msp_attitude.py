from . import _MspDataStructure, _Point2D, command_code, struct_format

from ..msp_commands import MSP_ATTITUDE

from typing import Self

@command_code(MSP_ATTITUDE)
@struct_format('3h')
class MspAttitude(_MspDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: _Point2D[float]

    heading: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspAttitude(data[0:2], data[2])
