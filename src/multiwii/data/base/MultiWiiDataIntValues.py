from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MultiWiiDataIntValues(MultiWiiData):
    """
    The base class for data values with a single, public int tuple member.
    """
    values: Final[Tuple[int]] = ()
