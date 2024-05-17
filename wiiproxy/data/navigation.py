from . import Coord2D

from dataclasses import dataclass

@dataclass
class MspCompGps:
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: int

    direction_to_home: int

    update: int

@dataclass
class MspRawGps:
    """Represents data values for the MSP_RAW_GPS command."""
    fix: int

    satellites: int

    coordinate: Coord2D[float]

    altitude: int

    speed: int

    ground_course: float

@dataclass
class MspWaypoint:
    """Represents data values for the MSP_WP command."""
    number: int

    coordinate: Coord2D[int]

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
