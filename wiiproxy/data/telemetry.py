from . import Point2D, Point3D

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspAltitude:
    """Represents data values for the MSP_ALTITUDE command.

    This class encapsulates altitude-related data from a MultiWii flight controller.

    Attributes
    ----------
    estimation : int
        The estimated altitude.
    pressure_variation : int
        The variation in pressure.
    """
    estimation: int

    pressure_variation: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspAltitude` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspAltitude
            An instance of the `MspAltitude` class populated with the parsed data.
        """
        return cls(*data)

@dataclass
class MspAttitude:
    """Represents data values for the MSP_ATTITUDE command.

    This class encapsulates attitude-related data from a MultiWii flight controller.

    Attributes
    ----------
    angle : Point2D[float]
        The angles in the pitch and roll axes.
    heading : int
        The heading angle.
    """
    angle: Point2D[float]

    heading: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspAttitude` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspAttitude
            An instance of the `MspAttitude` class populated with the parsed data.
        """
        return cls(
            angle=Point2D(
                x=data[0] / 10.0,
                y=data[1] / 10.0
            ),
            heading=data[3]
        )

@dataclass
class MspRawImu:
    """Represents data values for the MSP_RAW_IMU command.

    This class encapsulates raw IMU (Intertial Measurement Unit) data from a MultiWii
    flight controller.

    Attributes
    ----------
    acc : Point3D[float]
        The accelerometer data.
    gyro : Point3D[float]
        The gyroscope data.
    mag : Point3D[float]
        The magnetometer data.
    """
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
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspRawImu` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.
        acc_unit : int, optional
            The unit conversion factor for the accelerometer data (default is 1.0).
        gyro_unit : int, optional
            The unit conversion factor for the gyroscope data (default is 1.0).
        mag_unit : int, optional
            The unit conversion factor for the magnetometer data (default is 1.0).

        Returns
        -------
        MspRawImu
            An instance of the `MspRawImu` class populated with the parsed data.
        """
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
