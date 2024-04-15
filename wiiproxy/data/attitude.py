from ._base import _MultiWiiDataStructure

class Attitude(_MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""
    angle: tuple[int]

    heading: int
