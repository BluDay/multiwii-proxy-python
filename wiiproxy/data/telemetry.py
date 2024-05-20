from . import Point2D, Point3D

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspAltitude:
    """Represents data values for the MSP_ALTITUDE command."""
    estimation: int

    pressure_variation: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)

@dataclass
class MspAttitude:
    """Represents data values for the MSP_ATTITUDE command."""
    angle: Point2D[float]

    heading: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            angle=Point2D(
                x=data[0] / 10.0,
                y=data[1] / 10.0
            ),
            heading=data[3]
        )

@dataclass
class MspRawImu:
    """Represents data values for the MSP_RAW_IMU command."""
    acc: Point3D[float]

    gyro: Point3D[float]

    mag: Point3D[float]

    @classmethod
    def parse(
        cls,
        data:      tuple,
        acc_unit:  int = 1.0,
        gyro_unit: int = 1.0,
        mag_unit:  int = 1.0
    ) -> Self:
        return cls(
            acc=Point3D(
                x=data[0] / acc_unit,
                y=data[1] / acc_unit,
                z=data[2] / acc_unit
            ),
            gyro=Point3D(
                x=data[3] / gyro_unit,
                y=data[4] / gyro_unit,
                z=data[5] / gyro_unit
            ),
            mag=Point3D(
                x=data[6] / mag_unit,
                y=data[7] / mag_unit,
                z=data[8] / mag_unit
            )
        )
