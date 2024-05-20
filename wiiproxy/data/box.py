from ..config    import MultiWiiBox, MultiWiiBoxState
from ..messaging import decode_names

from dataclasses import dataclass
from typing      import NamedTuple, Self

@dataclass
class MspBox:
    """Represents data values for the MSP_BOX command.

    Attributes
    ----------
    values : tuple[int]
        The data values.
    """
    values: tuple[int]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(values=data)

@dataclass
class MspBoxIds:
    """Represents data values for the MSP_BOXIDS command.

    Attributes
    ----------
    values : tuple[MultiWiiBox]
        The data values as `MultiWiiBox`es.
    """
    values: tuple[MultiWiiBox]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        values = (MultiWiiBox(value) for value in data)

        return cls(values)

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
    """Represents data values for the MSP_BOXNAMES command.

    This class is used to store the names of various boxes that can be checked in a
    MultiWii flight controller. Each box corresponds to a specific function or mode
    that can be activated in the flight controller's configuration.
    
    Attributes
    ----------
    names : tuple[str]
        The name of the boxes as strings.
    """
    names: tuple[str]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(names=decode_names(data))
