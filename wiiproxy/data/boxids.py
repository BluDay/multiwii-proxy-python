from wiiproxy.config.box import MultiWiiBox

from wiiproxy.data._base import _MultiWiiDataStructure

@dataclass(slots=True)
class BoxIds(_MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Optional[tuple[MultiWiiBox]]
