from . import Point3D

from ._base import MultiWiiDataStructure

class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: Point3D

    gyro: Point3D

    mag: Point3D
