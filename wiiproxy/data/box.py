from ..config import MultiWiiBox, MultiWiiBoxState

from dataclasses import dataclass
from typing      import NamedTuple

@dataclass
class MspBox:
    """Represents data values for the MSP_BOX command."""
    values: tuple[int]

@dataclass
class MspBoxIds:
    """Represents data values for the MSP_BOXIDS command."""
    values: tuple[MultiWiiBox]

@dataclass
class MspBoxItem(NamedTuple):
    """Represents data values for the MSP_SET_BOX command."""
    aux1: MultiWiiBoxState
    aux2: MultiWiiBoxState
    aux3: MultiWiiBoxState
    aux4: MultiWiiBoxState
     
    def compile(self) -> int:
        """Compiles all of the set box state values to a single unsigned integer value."""
        pass

@dataclass
class MspBoxNames:
    """Represents data values for the MSP_BOXNAMES command."""
    names: tuple[str]
