from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Status(MultiWiiData):
    """
    Represents data values for the MSP_STATUS command.
    """
    cycle_time: Final[int] = 0

    i2c_errors: Final[int] = 0

    sensors: Final[Tuple[int]] = ()

    flag: Final[int] = 0

    global_conf: Final[int] = 0
