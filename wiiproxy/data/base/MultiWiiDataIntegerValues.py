from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final, Tuple

@dataclass(slots=True)
class MultiWiiDataIntegerValues(MultiWiiDataStructure):
    """The base MultiWii class for data values with a single, public int tuple member."""
    values: Final[Tuple[int] | None]
