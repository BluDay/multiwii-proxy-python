from ._base import MultiWiiDataStructure

class RawGps(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    fix: int

    satellites: int

    coordinates: tuple[int]

    altitude: int

    speed: int

    ground_course: int
