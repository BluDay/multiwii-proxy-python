from . import _MspDataStructure, command_code, struct_format

from ..config       import MultiWiiSensor
from ..msp_commands import MSP_STATUS

from typing import NoReturn

@command_code(MSP_STATUS)
@struct_format('3HIB')
class MspStatus(_MspDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int

    @staticmethod
    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        cycle_time = data[0]

        i2c_errors = data[1]

        sensors = ()

        for sensor in MultiWiiSensor:
            if sensor | data[2]:
                sensors += (sensor,)

        flag = data[3]

        global_conf = data[4]

        return MspStatus(
            cycle_time,
            i2c_errors,
            sensors,
            flag,
            global_conf
        )
