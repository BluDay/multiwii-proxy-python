from dataclasses import dataclass
from typing      import Self

@dataclass
class MspRc:
    """Represents data values for the MSP_RC command.
    
    This class encapsulates the RC (Remote Control) input values for various control axes
    in the MultiWii flight controller.

    Attributes
    ----------
    roll : int
        The input value for the roll axis.
    pitch : int
        The input value for the pitch axis.
    yaw : int
        The input value for the yaw axis.
    throttle : int
        The input value for the throttle.
    aux1 : int
        The input value for the first auxiliary channel.
    aux2 : int
        The input value for the second auxiliary channel.
    aux3 : int
        The input value for the third auxiliary channel.
    aux4 : int
        The input value for the fourth auxiliary channel.
    """
    roll: int

    pitch: int

    yaw: int

    throttle: int

    aux1: int

    aux2: int

    aux3: int

    aux4: int
    
    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspRc` class.

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

    Attributes
    ----------
    rate : int
        The RC rate.
    expo : int
        The RC expo.
    roll_pitch_rate : int
        The roll and pitch rate.
    yaw_rate : int
        The yaw rate.
    dynamic_throttle_pid : int
        The dynamic throttle PID.
    throttle_mid : int
        The throttle mid-point value.
    throttle_expo : int
        The throttle expo value.
    """
    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspRcTuning` class.

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
