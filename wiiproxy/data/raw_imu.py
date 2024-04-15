from . import Point3D

from ._base import command_code, struct_format, MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.RAW_IMU)
@struct_format('9h')
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D

    gyro: Point3D

    mag: Point3D
