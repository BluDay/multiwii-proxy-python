from ._base import _MultiWiiDataStructure

class RawGps(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""
    fix: int

    satellites: int

    coordinates: tuple[int]

    altitude: int

    speed: int

    ground_course: int
