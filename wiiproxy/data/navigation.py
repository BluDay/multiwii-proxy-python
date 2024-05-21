from . import Coords2D

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspCompGps:
    """Represents data values for the MSP_COMP_GPS command.

    This class encapsulates the GPS compass data from the MultiWii flight controller.
    It provides information about the distance and direction to the hime position, as
    well as the update status of the GPS data.

    Attributes
    ----------
    distance_to_home : int
        The distance to the home position in meters.
    direction_to_home : int
        The direction to the home position in degrees.
    update : int
        The update status of the GPS data.
    """
    distance_to_home: int

    direction_to_home: int

    update: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspCompGps` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspCompGps
            An instance of the `MspCompGps` class populated with the parsed data.
        """
        return cls(*data)

@dataclass
class MspRawGps:
    """Represents data values for the MSP_RAW_GPS command.
    
    This class encapsulates the GPS compass data from the MultiWii flight controller.
    It provides information about the 

    Attributes
    ----------
    fix : int
        The GPS fix status.
    satellites : int
        The number of satellites in view.
    coords : Coords2D[float]
        The GPS coordinates (latitude and longitude).
    altitude : int
        The altitude in meters.
    speed : int
        The speed in cm/s.
    ground_course : float
        The ground course in degrees.
    """
    fix: int

    satellites: int

    coords: Coords2D[float]

    altitude: int

    speed: int

    ground_course: float

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspRawGps` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspRawGps
            An instance of the `MspRawGps` class populated with the parsed data.
        """
        return cls(
            fix=data[0],
            satellites=data[1],
            coords=Coords2D(
                latitude=data[2] / 10000000.0,
                longitude=data[3] / 10000000.0
            ),
            altitude=data[4],
            speed=[5],
            ground_course=data[6] / 10.0
        )

@dataclass
class MspWaypoint:
    """Represents data values for the MSP_WP command.

    This class encapsulates the waypoint data from the MultiWii flight controller.
    It provides information about the waypoint number, coordinates, altitude hold,
    heading, time to stay at the waypoint, and the waypoint flag.

    Attributes
    ----------
    number : int
        The waypoint number.
    coords : Coords2D[int]
        The GPS coordinates (latitude and longitude) of the waypoint.
    alt_hold : int
        The altitude hold value in meters.
    heading : int
        The heading in degrees.
    time_to_stay : int
        The time to stay at the waypoint in seconds.
    flag : int
        The waypoint flag indicating the waypoint's status or type.
    """
    number: int

    coords: Coords2D[int]

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspWaypoint` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspWaypoint
            An instance of the `MspWaypoint` class populated with the parsed data.
        """
        return cls(
            number=data[0],
            coords=Coords2D(
                latitude=data[1] / 10000000.0,
                longitude=data[2] / 10000000.0
            ),
            alt_hold=data[3],
            heading=data[4],
            time_to_stay=data[5],
            flag=data[6]
        )
