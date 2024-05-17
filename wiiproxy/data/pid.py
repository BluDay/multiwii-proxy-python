from . import PidValues

from dataclasses import dataclass

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

@dataclass
class MspPidNames:
    """Represents data values for the MSP_PIDNAMES command."""
    names: tuple[str]
