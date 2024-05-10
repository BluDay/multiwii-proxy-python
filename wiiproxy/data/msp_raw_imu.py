from . import _MspDataStructure, _Point3D, command_code, struct_format

from ..msp_commands import MSP_RAW_IMU

from typing import Self

@command_code(MSP_RAW_IMU)
@struct_format('9h')
class MspRawImu(_MspDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc: _Point3D[float]

    gyro: _Point3D[float]

    mag: _Point3D[float]

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        return MspRawImu(data[0:3], data[3:6], data[6:9])
