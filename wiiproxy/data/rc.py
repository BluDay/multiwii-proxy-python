from ._base import MultiWiiDataStructure

class Rc(MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""

    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]
