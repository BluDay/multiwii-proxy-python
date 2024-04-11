from wiiproxy.config    import MultiWiiCapability, MultiWiiMultitype
from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Final[float | None]

    multitype: Final[MultiWiiMultitype | None]

    capabilities: Final[Tuple[MultiWiiCapability] | None]

    navi_version: Final[int | None]
