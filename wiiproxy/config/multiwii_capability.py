from enum   import IntEnum, unique
from typing import Self

@unique
class MultiWiiCapability(IntEnum):
    """Represents various capabilities of a MultiWii flight controller.

    Each capability indicates a specific feature that the flight controller supports.
    """
    Bind   = 0b00001
    Dynbal = 0b00010
    Flap   = 0b00100
    Nav    = 0b01000
    ExtAux = 0b10000

    @classmethod
    def get_capabilities(cls, value: int) -> tuple[Self]:
        """Parses and returns all capability flags from a given integer.
   
        This method identifies which capabilities are enabled by performing a
        bitwise AND operation with each capability type.
        """
        capabilities = ()

        for capability in cls:
            if capability & value:
                capabilities += (capability,)

        return capabilities
