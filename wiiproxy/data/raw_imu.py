from . import Point3D

from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.RAW_IMU)
@MultiWiiDataStructure.struct_format('9h')
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D

    gyro: Point3D

    mag: Point3D
