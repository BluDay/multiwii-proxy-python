from . import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MultiWiiDataIntegerValues(MultiWiiDataStructure):
    """The base class for data values with a single, public int tuple member."""
    values: Final[Tuple[int]] = ()
