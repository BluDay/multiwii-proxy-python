from wiiproxy.config.box import MultiWiiBox

from wiiproxy.data._values import (
    _MultiWiiDataIntegerValues,
    _MultiWiiDataStringValues,
    _MultiWiiDataStructure
)

class Box(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_BOX command."""
    pass

@dataclass(slots=True)
class BoxIds(_MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Optional[tuple[MultiWiiBox]]

class BoxNames(_MultiWiiDataStringValues):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
