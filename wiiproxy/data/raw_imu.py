from . import Point3D

from ._base import msp_command_code, msp_data_struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@msp_command_code(MspCommands.RAW_IMU)
@msp_data_struct_format('9h')
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D

    gyro: Point3D

    mag: Point3D
