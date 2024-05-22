from . import Point3D

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
    pitch_angle : float
        The pitch angle of the aircraft in degrees, ranging from -180 to 180.
    roll_angle : float
        The roll angle of the aircraft in degrees, ranging from -90 to 90.
    yaw_angle : int
        The heading angle of the aircraft in degrees, ranging from 0 to 360.
    """
    pitch_angle: float

    roll_angle: float

    yaw_angle: int

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
            pitch_angle=data[0] / 10.0,
            roll_angle=data[1] / 10.0,
            yaw_angle=data[3]
        )

@dataclass
class MspRawImu:
    """Represents data values for the MSP_RAW_IMU command.

    This class encapsulates raw IMU (Intertial Measurement Unit) data from a MultiWii
    flight controller.

    Attributes
    ----------
    accelerometer : Point3D[float]
        The accelerometer data.
    gyroscope : Point3D[float]
        The gyroscope data.
    magnetometer : Point3D[float]
        The magnetometer data.
    """
    accelerometer: Point3D[float]

    gyroscope: Point3D[float]

    magnetometer: Point3D[float]

    @classmethod
    def parse(
        cls,
        data:               tuple,
        accelerometer_unit: int = 1.0,
        gyroscope_unit:     int = 1.0,
        magnetometer_unit:  int = 1.0
    ) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspRawImu` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.
        accelerometer_unit : int, optional
            The unit conversion factor for the accelerometer data (default is 1.0).
        gyroscope_unit : int, optional
            The unit conversion factor for the gyroscope data (default is 1.0).
        magnetometer_unit : int, optional
            The unit conversion factor for the magnetometer data (default is 1.0).

        Returns
        -------
        MspRawImu
            An instance of the `MspRawImu` class populated with the parsed data.
        """
        return cls(
            accelerometer=Point3D(
                x=data[0] / accelerometer_unit,
                y=data[1] / accelerometer_unit,
                z=data[2] / accelerometer_unit
            ),
            gyroscope=Point3D(
                x=data[3] / gyroscope_unit,
                y=data[4] / gyroscope_unit,
                z=data[5] / gyroscope_unit
            ),
            magnetometer=Point3D(
                x=data[6] / magnetometer_unit,
                y=data[7] / magnetometer_unit,
                z=data[8] / magnetometer_unit
            )
        )
