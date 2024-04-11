from dataclasses import dataclass
from typing      import Optional

class _MultiWiiDataStructure(object):
    """Represents the base class for MSP data structure classes."""
    pass

@dataclass(slots=True)
class _MultiWiiDataIntegerValues(_MultiWiiDataStructure):
    """The base MultiWii class for data values with a single, public int tuple member."""
    values: Optional[tuple[int]]

@dataclass(slots=True)
class _MultiWiiDataStringValues(_MultiWiiDataStructure):
    """The base class for data values with a single, public string tuple member."""
    values: Optional[tuple[str]]
