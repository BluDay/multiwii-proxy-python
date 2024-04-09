from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Motor(MultiWiiData):
    """
    Represents data values for the MSP_MOTOR command.
    """
    values: Final[Tuple[int]] = ()
