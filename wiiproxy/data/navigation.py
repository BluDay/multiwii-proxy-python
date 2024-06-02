from . import Coords2D

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspCompGps:
    """
    Represents data values for the MSP_COMP_GPS command.

    This class encapsulates the GPS compass data from the MultiWii flight controller.
    It provides information about the distance and direction to the hime position, as
    well as the update status of the GPS data.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    distance_to_home: int
    """int: The distance to the home position in meters."""

    direction_to_home: int
    """int: The direction to the home position in degrees."""

    update_status: int
    """int: The update status of the GPS data."""
    
    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspCompGps` class.

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
    """
    Represents data values for the MSP_RAW_GPS command.
    
    This class encapsulates the GPS compass data from the MultiWii flight controller.
    It provides information about the GPS fix status, number of satellites in view,
    coordinates (latitude and longitude), altitude, speed, and ground course.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------
    
    fix: int
    """int: The GPS fix status."""

    satellites: int
    """int: The number of satellites in view."""

    coordinates: Coords2D[float]
    """Coords2D[float]: The GPS coordinates (latitude and longitude)."""

    altitude: int
    """int: The altitude in meters."""

    speed: int
    """int: The speed in cm/s."""

    ground_course: float
    """float: The ground course in degrees."""
    
    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspRawGps` class.

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
            coordinates=Coords2D(
                latitude=data[2] / 10000000.0,
                longitude=data[3] / 10000000.0
            ),
            altitude=data[4],
            speed=[5],
            ground_course=data[6] / 10.0
        )

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def as_serializable(self) -> tuple[int]:
        """
        Returns a tuple with integer values to be used for serialization.

        Returns
        -------
        tuple[int]
            A tuple with serializable integer values.
        """
        return (
            fix,
            satellites,
            int(coordinates.latitude * 10000000),
            int(coordinates.longitude * 10000000),
            altitude,
            speed,
            int(ground_course * 10)
        )

@dataclass
class MspWaypoint:
    """
    Represents data values for the MSP_WP command.

    This class encapsulates the waypoint data from the MultiWii flight controller.
    It provides information about the waypoint number, coordinates, altitude hold,
    heading, time to stay at the waypoint, and the waypoint flag.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    number: int
    """int: The waypoint number."""

    coordinates: Coords2D[int]
    """Coords2D[int]: The GPS coordinates (latitude and longitude) of the waypoint."""

    altitude_hold: int
    """int: The altitude hold value in meters."""

    heading: int
    """int: The heading in degrees."""

    time_to_stay: int
    """int: The time to stay at the waypoint in seconds."""

    status_flag: int
    """int: The waypoint flag indicating the waypoint's status or type."""
    
    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspWaypoint` class.

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
            coordinates=Coords2D(
                latitude=data[1] / 10000000.0,
                longitude=data[2] / 10000000.0
            ),
            altitude_hold=data[3],
            heading=data[4],
            time_to_stay=data[5],
            status_flag=data[6]
        )

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def as_serializable(self) -> tuple[int]:
        """
        Returns a tuple with integer values to be used for serialization.

        Returns
        -------
        tuple[int]
            A tuple with serializable integer values.
        """
        return (
            number,
            int(coordinates.latitude * 100000000),
            int(coordinates.longitude * 100000000),
            altitude_hold,
            heading,
            time_to_stay,
            status_flag
        )
