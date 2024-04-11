from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final, Tuple

@dataclass(slots=True)
class MultiWiiDataStringValues(MultiWiiDataStructure):
    """The base class for data values with a single, public string tuple member."""
    values: Final[Tuple[str] | None]
