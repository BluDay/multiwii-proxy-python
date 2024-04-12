from ._base import _MultiWiiDataStructure

from ..config.capability import MultiWiiCapability
from ..config.multitype  import MultiWiiMultitype

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Ident(_MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: Optional[float]

    multitype: Optional[MultiWiiMultitype]

    capabilities: Optional[tuple[MultiWiiCapability]]

    navi_version: Optional[int]
