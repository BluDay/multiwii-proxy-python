from . import Point3D

from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

@msp_command_code(102)
@msp_data_struct_format('9h')
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D

    gyro: Point3D

    mag: Point3D
