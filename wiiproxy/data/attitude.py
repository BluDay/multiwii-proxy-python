from ._base import MultiWiiDataStructure

class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: tuple[int]

    heading: int
