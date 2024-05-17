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
    """Represents data values for the MSP_SET_BOX command.

    This class encapsulates the configuration of auxiliary (aux) control boxes in a
    MultiWii flight controller. Each box can be assigned a specific function or mode,
    and its state can be set to the following values:

        * (Unselected) (Empty)
        * LOW (Low)
        * MID (Mid)
        * HIGH (High)

    Attributes
    ----------
    aux 1: MultiWiiStateBox
        The state value for the first auxiliary function.
    aux 2: MultiWiiStateBox
        The state value for the second auxiliary function.
    aux 3: MultiWiiStateBox
        The state value for the third auxiliary function.
    aux 4: MultiWiiStateBox
        The state value for the fourth auxiliary function.   
    """
    aux1: MultiWiiBoxState
    aux2: MultiWiiBoxState
    aux3: MultiWiiBoxState
    aux4: MultiWiiBoxState
     
    def compile(self) -> int:
        """Compiles all of the box state values into a single unsigned integer value.

        Returns
        -------
        int
            The compiled integer value representing the combined state of all auxiliary
            control boxes.
        """
        pass

@dataclass
class MspBoxNames:
    """Represents data values for the MSP_BOXNAMES command."""
    names: tuple[str]
