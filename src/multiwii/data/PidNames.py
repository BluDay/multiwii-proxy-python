from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class PidNames(MultiWiiData):
    """
    Represents data values for the MSP_PIDNAMES command.
    """
    values: Final[Tuple[str]] = ()
