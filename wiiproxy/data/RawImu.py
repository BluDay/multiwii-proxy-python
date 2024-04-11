from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc:  Final[Tuple[int] | None]
    gyro: Final[Tuple[int] | None]
    mag:  Final[Tuple[int] | None]
