from wiiproxy.data.base.MultiWiiDataStructure import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc:  Final[tuple[int] | None]
    gyro: Final[tuple[int] | None]
    mag:  Final[tuple[int] | None]
