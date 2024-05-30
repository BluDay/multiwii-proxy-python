from dataclasses import dataclass
from typing      import Self

@dataclass
class MspRc:
    """Represents data values for the MSP_RC command.
    
    This class encapsulates the RC (Remote Control) input values for various control axes in
    the MultiWii flight controller.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    roll: int
    """int: The input value for the roll axis."""

    pitch: int
    """int: The input value for the pitch axis."""

    yaw: int
    """int: The input value for the yaw axis."""

    throttle: int
    """int: The input value for the throttle."""

    aux1: int
    """int: The input value for the first auxiliary channel."""

    aux2: int
    """int: The input value for the second auxiliary channel."""

    aux3: int
    """int: The input value for the third auxiliary channel."""

    aux4: int
    """int: The input value for the fourth auxiliary channel."""
    
    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an instance
        of the `MspRc` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspRc
            An instance of the `MspRc` class populated with the parsed data.
        """
        return cls(*data)

@dataclass
class MspRcTuning:
    """Represents data values for the MSP_RC_TUNING command.

    This class encapsulates the tuning parameters for the RC (Remote Control) inputs
    in the MultiWii flight controller. It provides information about the rates, expo,
    and throttle settings.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    rate: int
    """int: The RC rate."""

    expo: int
    """int: The RC expo."""

    roll_pitch_rate: int
    """int: The roll and pitch rate."""

    yaw_rate: int
    """int: The yaw rate."""

    dynamic_throttle_pid: int
    """int: The dynamic throttle PID."""

    throttle_mid: int
    """int: The throttle mid-point value."""

    throttle_expo: int
    """int: The throttle expo value."""

    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an instance
        of the `MspRcTuning` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspRcTuning
            An instance of the `MspRcTuning` class populated with the parsed data.
        """
        return cls(*data)
