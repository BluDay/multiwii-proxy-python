from . import Pid

from ..messaging import _decode_names

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspPid:
    """
    Represents data values for the MSP_PID command.

    This class encapsulates the PID controller settings for various control axes and functions
    in the MultiWii flight controller.
    """
    roll: Pid[int]
    """Pid[int]: PID values for the roll axis."""

    pitch: Pid[int]
    """Pid[int]: PID values for the pitch axis."""

    yaw: Pid[int]
    """Pid[int]: PID values for the yaw axis."""

    altitude_hold: Pid[int]
    """Pid[int]: PID values for the altitude hold."""

    position_hold: Pid[int]
    """Pid[int]: PID values for the position hold."""

    position_rate: Pid[int]
    """Pid[int]: PID values for the position rate."""

    navigation_rate: Pid[int]
    """Pid[int]: PID values for the navigation rate."""

    level_mode: Pid[int]
    """Pid[int]: PID values for the level mode."""

    magnetometer: Pid[int]
    """Pid[int]: PID values for the magnetometer."""

    velocity: Pid[int]
    """Pid[int]: PID values for the velocity."""
   
    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspPid` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspPid
            An instance of the `MspPid` class populated with the parsed data.
        """
        pid_collection = ()

        for index in range(len(data), step=3):
            pid = Pid(
                p=data[index],
                i=data[index + 1],
                d=data[index + 2]
            )

            pid_collection += (pid,)

        return cls(*pid_collection)

    def as_serializable(self) -> tuple[int]:
        """
        Returns a tuple with integer values to be used for serialization.

        Returns
        -------
        tuple[int]
            A tuple with serializable integer values.
        """
        return (
            roll.p,
            roll.i,
            roll.d,

            pitch.p,
            pitch.i,
            pitch.d,

            yaw.p,
            yaw.i,
            yaw.d,

            altitude_hold.p,
            altitude_hold.i,
            altitude_hold.d,

            position_hold.p,
            position_hold.i,
            position_hold.d,

            position_rate.p,
            position_rate.i,
            position_rate.d,

            navigation_rate.p,
            navigation_rate.i,
            navigation_rate.d,

            level_mode.p,
            level_mode.i,
            level_mode.d,

            magnetometer.p,
            magnetometer.i,
            magnetometer.d,

            velocity.p,
            velocity.i,
            velocity.d
        )

@dataclass
class MspPidNames:
    """
    Represents data values for the MSP_PIDNAMES command.

    This class is used to store the names of various PID controllers used in the MultiWii
    flight controller. Each name corresponds to a specific PID controller setting.
    """
    names: tuple[str]
    """tuple[str]: The names of the PID controllers."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspPidNames` class.

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
