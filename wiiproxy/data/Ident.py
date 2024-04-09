from .base    import MspDataStructure
from ..config import MspCapabilityType, MspMultitypeType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MspDataStructure):
    """
    Represents data values for the MSP_IDENT command.
    """
    version: Final[float] = 0.0

    multitype: Final[MspMultitypeType] = MspMultitypeType.Unidentified

    capabilities: Final[Tuple[MspCapabilityType]] = ()

    navi_version: Final[int] = 0
