from . import Point2D, Point3D

from dataclasses import dataclass

@dataclass
class MspAltitude:
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: int

    pressure_variation: int

@dataclass
class MspAttitude:
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Point2D[float]

    heading: int

@dataclass
class MspRawImu:
    """Represents data values for the MSP_RAW_IMU command."""
    acc: Point3D[float]

    gyro: Point3D[float]

    mag: Point3D[float]
