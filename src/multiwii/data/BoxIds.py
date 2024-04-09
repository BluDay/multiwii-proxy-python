from .        import MultiWiiData
from ..config import BoxType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class BoxIds(MultiWiiData):
    """
    Represents data values for the MSP_BOXIDS command.
    """
    values: Final[Tuple[BoxType]] = ()
