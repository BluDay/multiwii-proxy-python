from . import command_code, struct_format, MultiWiiData, Point3D

from ..messaging import MspCommands

@command_code(MspCommands.RAW_IMU)
@struct_format('9h')
class RawImu(MultiWiiData):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D[float]

    gyro: Point3D[float]

    mag: Point3D[float]
