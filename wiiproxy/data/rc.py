from dataclasses import dataclass
from typing      import Self

@dataclass
class MspRc:
    """Represents data values for the MSP_RC command."""
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
        return cls(*data)

@dataclass
class MspRcTuning:
    """Represents data values for the MSP_RC_TUNING command."""
    rate: int

    expo: int

    roll_pitch_rate: int

    yaw_rate: int

    dynamic_throttle_pid: int

    throttle_mid: int

    throttle_expo: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)
