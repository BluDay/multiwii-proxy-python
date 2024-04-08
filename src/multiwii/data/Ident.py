from .base    import _MultiWiiData
from ..config import CapabilityType, VehicleType

from dataclasses import dataclass

@dataclass(slots=True)
class Ident(_MultiWiiData):
    """
    Represents data values for the MSP_IDENT command.
    """
    version: float = 0.0

    multitype: VehicleType = VehicleType.Unidentified

    capabilities: Tuple[CapabilityType] = ()

    navi_version: int = 0

    def update_values(self, data: tuple) -> None:
        """
        Overridden method.
        """
        self.version = data[0] / 100

        self.multitype = VehicleType(data[1])
        
        self.capabilities = (
            capability if capability & data[3] for capability in CapabilityType
        )

        self.navi_version = data[3] >> 28

        super().update_values(data)
