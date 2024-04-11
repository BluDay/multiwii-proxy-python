from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MultiWiiDataStringValues(MultiWiiDataStructure):
    """The base class for data values with a single, public string tuple member."""
    values: Final[tuple[str] | None]
