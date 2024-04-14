from . import _MultiWiiDataStructure

from ..config.multiwii_box import MultiWiiBox

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class BoxIds(_MultiWiiDataStructure):
    """Represents data values for the MSP_BOXIDS command."""
    values: Optional[tuple[MultiWiiBox]]
