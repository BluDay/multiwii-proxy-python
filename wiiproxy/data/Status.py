from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Status(MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: Final[int | None]

    i2c_errors: Final[int | None]

    sensors: Final[tuple[int] | None]

    flag: Final[int | None]

    global_conf: Final[int | None]
