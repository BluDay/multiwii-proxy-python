from . import MspDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MspDataStructureStringValues(MspDataStructure):
    """
    The base class for data values with a single, public string tuple member.
    """
    values: Final[Tuple[str]] = ()
