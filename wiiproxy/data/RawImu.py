from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final, Tuple

@dataclass(slots=True)
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc:  Final[Tuple[int] | None]
    gyro: Final[Tuple[int] | None]
    mag:  Final[Tuple[int] | None]
