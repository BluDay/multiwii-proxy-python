from . import _MspDataStructure, command_code, struct_format

from ..msp_commands import MSP_ANALOG

from typing import Self

@command_code(MSP_ANALOG)
@struct_format('B3H')
class MspAnalog(_MspDataStructure):
    """Represents data values for the MSP_ANALOG command."""
    voltage: int

    power_meter_sum: int

    rssi: int

    amperage: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        self._voltage         = data[0] / 10
        self._power_meter_sum = data[1]
        self._rssi            = data[2]
        self._amperage        = data[3]
