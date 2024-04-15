from ._base import _MultiWiiDataStructure

class Waypoint(_MultiWiiDataStructure):
    """Represents data values for the MSP_WP command."""
    number: int

    position: tuple[int]

    alt_hold: int

    heading: int

    time_to_stay: int

    flag: int
