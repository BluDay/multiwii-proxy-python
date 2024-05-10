from . import _MspValues, command_code, struct_format

from ..config       import MultiWiiBox
from ..msp_commands import MSP_BOXIDS

from typing import Self

@command_code(MSP_BOXIDS)
@struct_format('B', has_variable_size=True)
class MspBoxIds(_MspValues):
    """Represents data values for the MSP_BOXIDS command."""
    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        values = tuple(BoxType(value) for value in data)

        return MspBoxIds(values)
