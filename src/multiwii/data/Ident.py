from .base    import MspDataStructure
from ..config import CapabilityType, VehicleType

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class Ident(MspDataStructure):
    """
    Represents data values for the MSP_IDENT command.
    """
    version: Final[float] = 0.0

    multitype: Final[VehicleType] = VehicleType.Unidentified

    capabilities: Final[Tuple[CapabilityType]] = ()

    navi_version: Final[int] = 0
