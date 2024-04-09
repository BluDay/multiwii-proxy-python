from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class BoxNames(MultiWiiData):
    """
    Represents data values for the MSP_BOXNAMES command.
    """
    values: Final[Tuple[str]] = ()
