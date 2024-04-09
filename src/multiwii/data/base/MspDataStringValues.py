from . import MspDataType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class MspDataStringValues(MspDataType):
    """
    The base class for data values with a single, public string tuple member.
    """
    values: Final[Tuple[str]] = ()
