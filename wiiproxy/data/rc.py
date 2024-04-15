from ._base import _MultiWiiDataStructure

class Rc(_MultiWiiDataStructure):
    """Represents data values for the MSP_RC command."""
    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux: tuple[int]
