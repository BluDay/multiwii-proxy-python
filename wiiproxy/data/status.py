from ._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class Status(_MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: Optional[int]

    i2c_errors: Optional[int]

    sensors: Optional[tuple[int]]

    flag: Optional[int]

    global_conf: Optional[int]
