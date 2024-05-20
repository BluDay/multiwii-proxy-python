from . import Coord2D

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspCompGps:
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: int

    direction_to_home: int

    update: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)

@dataclass
class MspRawGps:
    """Represents data values for the MSP_RAW_GPS command."""
    fix: int

    satellites: int

    coordinate: Coord2D[float]

    altitude: int

    speed: int

    ground_course: float

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            fix=data[0],
            satellites=data[1],
            coordinate=Coord2D(
                latitude=data[2] / 10000000.0,
                longitude=data[3] / 10000000.0
            ),
            altitude=data[4],
            speed=[5],
            ground_course=data[6] / 10.0
        )

@dataclass
class MspWaypoint:
    """Represents data values for the MSP_WP command."""
    number: int

    coordinate: Coord2D[int]

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(
            number=data[0],
            coordinate=Coord2D(
                latitude=data[1] / 10000000.0,
                longitude=data[2] / 10000000.0
            ),
            alt_hold=data[3],
            heading=data[4],
            time_to_stay=data[5],
            flag=data[6]
        )
