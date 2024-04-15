from ._base import MultiWiiDataStructure

class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""

    distance_to_home: int

    direction_to_home: int

    update: int # What?
