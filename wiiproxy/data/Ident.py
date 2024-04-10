from .base    import MultiWiiDataStructure
from ..config import MultiWiiCapability, MultiWiiMultitype

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Final[float] = 0.0

    multitype: Final[MultiWiiMultitype] = MultiWiiMultitype.Unidentified

    capabilities: Final[Tuple[MultiWiiCapability]] = ()

    navi_version: Final[int] = 0
