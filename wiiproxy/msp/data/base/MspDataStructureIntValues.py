from . import MspDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MspDataStructureIntValues(MspDataStructure):
    """
    The base class for data values with a single, public int tuple member.
    """
    values: Final[Tuple[int]] = ()
