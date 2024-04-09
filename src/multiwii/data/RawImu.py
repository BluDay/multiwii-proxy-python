from .base import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class RawImu(MultiWiiData):
    """
    Represents data values for the MSP_RAW_IMU command.
    """
    acc:  Final[Tuple[int]] = (0, 0, 0)
    gyro: Final[Tuple[int]] = (0, 0, 0)
    mag:  Final[Tuple[int]] = (0, 0, 0)
