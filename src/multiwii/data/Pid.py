from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Pid(MultiWiiData):
    """
    Represents data values for the MSP_PID command.
    """
    values: Final[Tuple[int]] = ()
