from .base    import MultiWiiDataStructure
from ..config import MultiWiiCapabilityType, MultiWiiMultitypeType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Final[float] = 0.0

    multitype: Final[MultiWiiMultitypeType] = MultiWiiMultitypeType.Unidentified

    capabilities: Final[Tuple[MultiWiiCapabilityType]] = ()

    navi_version: Final[int] = 0
