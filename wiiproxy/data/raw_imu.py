from ._base import _MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Optional

@dataclass(slots=True)
class RawImu(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc: Optional[tuple[int]]

    gyro: Optional[tuple[int]]

    mag: Optional[tuple[int]]
