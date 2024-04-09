from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Box(MultiWiiData):
    """
    represents data values for the msp_box command.
    """
    values: Final[Tuple[int]] = ()
