from ..config    import MultiWiiBox, MultiWiiBoxState
from ..messaging import _decode_names

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspBoxItem:
    """
    Represents data values for the MSP_SET_BOX command.

    This class encapsulates the configuration of auxiliary (aux) control boxes in a MultiWii
    flight controller. Each box can be assigned a specific function or mode, and its state can
    be set to the following values:

        * Empty (0b000) (Unselected)
        * Low   (0b001) (LOW)
        * Mid   (0b010) (MID)
        * High  (0b100) (HIGH)
    """
    aux1: MultiWiiBoxState
    """MultiWiiStateBox: The state value for the first auxiliary function."""

    aux2: MultiWiiBoxState
    """MultiWiiStateBox: The state value for the second auxiliary function."""

    aux3: MultiWiiBoxState
    """MultiWiiStateBox: The state value for the third auxiliary function."""

    aux4: MultiWiiBoxState
    """MultiWiiStateBox: The state value for the fourth auxiliary function."""

    @classmethod
    def parse(cls, value: int) -> Self:
        """
        Parses all auxiliary state values from the given parameter and instantiates an instance
        with the parsed state values.

        Parameters
        ----------
        value : int
            A single integer value consisting of all of the auxiliary states.

        Returns
        -------
        MspBoxItem
            An instance of the `MspBoxItem` class with parsed box item state values.
        """
        return cls(
            aux1=MultiWiiBoxState(value & 0x7),
            aux2=MultiWiiBoxState((value >> 3) & 0x7),
            aux3=MultiWiiBoxState((value >> 6) & 0x7),
            aux4=MultiWiiBoxState((value >> 9) & 0x7)
        )

    def compile(self) -> int:
        """
        Compiles all of the box state values into a single unsigned integer value.

        Returns
        -------
        int
            The compiled integer value representing the combined state of all auxiliary control
            boxes.
        """
        return self.aux1 | self.aux2 << 3 | self.aux3 << 6 | self.aux4 << 9

@dataclass
class MspBox:
    """
    Represents data values for the MSP_BOX command.

    This class is used to store the state values of various control boxes in a MultiWii flight
    controller. Control boxes can be used to enable or disable specific functions or modes
    during flight.
    """
    items: tuple[MspBoxItem]
    """tuple[MspBoxItem]: A tuple with the box items."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance
        of the `MspBox` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspBox
            An instance of the `MspBox` class populated with the parsed data.
        """
        return cls(tuple(MspBoxItem.parse(state) for state in data))
    
    def as_serializable(self) -> tuple[int]:
        """
        Returns a tuple with integer values to be used for serialization.

        Returns
        -------
        tuple[int]
            A tuple with serializable integer values.
        """
        return (box_item.compile() for box_item in self.values)

@dataclass
class MspBoxIds:
    """Represents data values for the MSP_BOXIDS command."""
    values: tuple[MultiWiiBox]
    """tuple[MultiWiiBox]: A tuple with `MultiWiiBox` values."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspBoxIds` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspBoxIds
            An instance of the `MspBoxIds` class populated with the parsed data.
        """
        return cls(tuple(MultiWiiBox(value) for value in data))

@dataclass
class MspBoxNames:
    """
    Represents data values for the MSP_BOXNAMES command.

    This class is used to store the names of various boxes that can be checked in a MultiWii
    flight controller. Each box corresponds to a specific function or mode that can be
    activated in the flight controller's configuration.
    """
    names: tuple[str]
    """tuple[str]: The name of the boxes as strings."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspBoxNames` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspBoxNames
            An instance of the `MspBoxNames` class populated with the parsed data.
        """
        return cls(decode_names(data))