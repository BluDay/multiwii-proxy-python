from wiiproxy.config                          import MultiWiiCapability, MultiWiiMultitype
from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Final[float | None]

    multitype: Final[MultiWiiMultitype]

    capabilities: Final[tuple[MultiWiiCapability] | None]

    navi_version: Final[int | None]
