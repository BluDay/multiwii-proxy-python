from .base    import MultiWiiDataStructure
from ..config import MultiWiiBoxType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class BoxIds(MultiWiiDataStructure):
    """
    Represents data values for the MSP_BOXIDS command.
    """
    values: Final[Tuple[MultiWiiBoxType]] = ()
