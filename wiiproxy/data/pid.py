from . import PidValues

from ..messaging import decode_names

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspPid:
    """Represents data values for the MSP_PID command."""
    roll: PidValues[int]

    pitch: PidValues[int]

    yaw: PidValues[int]

    alt: PidValues[int]

    pos: PidValues[int]

    posr: PidValues[int]

    navr: PidValues[int]

    level: PidValues[int]

    mag: PidValues[int]

    vel: PidValues[int]

    @classmethod
    def parse(cls, data: tuple) -> Self:
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
    """Represents data values for the MSP_PIDNAMES command."""
    names: tuple[str]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(names=decode_names(data))
