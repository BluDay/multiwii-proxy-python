from . import Point2D

from ._base import MultiWiiDataStructure

class Attitude(MultiWiiDataStructure):
    """Represents data values for the MSP_ATTITUDE command."""

    angle: Point2D

    heading: int
