from enum   import IntEnum, unique
from typing import Self

@unique
class MultiWiiCapability(IntEnum):
    """Represents some capabilities that the flight controller has."""
    Bind   = 0b0000001
    Dynbal = 0b0000010
    Flap   = 0b0000100
    Nav    = 0b0001000
    ExtAux = 0b0010000

    def get_capabilities(value: int) -> tuple[Self]:
        """Parses all capability values from a single integer."""
        capabilities = ()

        for capability in MultiWiiCapability:
            if capability & value:
                capabilities += (capability,)

        return capabilities
