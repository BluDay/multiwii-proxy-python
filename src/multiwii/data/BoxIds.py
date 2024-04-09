from .base    import MspDataType
from ..config import BoxType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class BoxIds(MspDataType):
    """
    Represents data values for the MSP_BOXIDS command.
    """
    values: Final[Tuple[BoxType]] = ()
