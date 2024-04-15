from . import Point2D

from ._base import MultiWiiDataStructure

class Waypoint(MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""

    number: int

    position: Point2D

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
