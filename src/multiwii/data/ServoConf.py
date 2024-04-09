from . import MultiWiiData

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class ServoConf(MultiWiiData):
    """
    Represents data values for the MSP_SERVO_CONF command.
    """
    values: Final[Tuple[int]] = ()
