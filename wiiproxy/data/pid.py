from . import PidValues

from ..messaging import _decode_names

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspPid:
    """Represents data values for the MSP_PID command.

    This class encapsulates the PID controller settings for various control axes and functions
    in the MultiWii flight controller.

    Attributes
    ----------
    roll : PidValues[int]
        The PID values for the roll axis.
    pitch : PidValues[int]
        The PID values for the pitch axis.
    yaw : PidValues[int]
        The PID values for the yaw axis.
    altitude_hold : PidValues[int]
        The PID values for the altitude hold.
    position_hold : PidValues[int]
        The PID values for the position hold.
    position_rate : PidValues[int]
        The PID values for the position rate.
    navigation_rate : PidValues[int]
        The PID values for the navigation rate.
    level_mode : PidValues[int]
        The PID values for the level mode.
    magnetometer : PidValues[int]
        The PID values for the magnetometer.
    velocity : PidValues[int]
        The PID values for the velocity.
    """
    roll: PidValues[int]

    pitch: PidValues[int]

    yaw: PidValues[int]

    altitude_hold: PidValues[int]

    position_hold: PidValues[int]

    position_rate: PidValues[int]

    navigation_rate: PidValues[int]

    level_mode: PidValues[int]

    magnetometer: PidValues[int]

    velocity: PidValues[int]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspPid` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspPid
            An instance of the `MspPid` class populated with the parsed data.
        """
        pid_values_collection = ()

        for index in range(len(data), step=3):
            pid_values = PidValues(
                p=data[index],
                i=data[index + 1],
                d=data[index + 2]
            )

            pid_values_collection += (pid_values,)

        return cls(*pid_values_collection)

@dataclass
class MspPidNames:
    """Represents data values for the MSP_PIDNAMES command.

    This class is used to store the names of various PID controllers used in the MultiWii
    flight controller. Each name corresponds to a specific PID controller setting.

    Attributes
    ----------
    names : tuple[str]
        The names of the PID controllers.
    """
    names: tuple[str]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspPidNames` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspPidNames
            An instance of the `MspPidNames` class populated with the parsed data.
        """
        return cls(decode_names(data))
