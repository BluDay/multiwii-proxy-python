from enum   import IntEnum, unique
from typing import Self

@unique
class MultiWiiSensor(IntEnum):
    """Represents different sensor types."""
    Acc   = 0
    Baro  = 1
    Mag   = 2
    Gps   = 3
    Sonar = 4

    @staticmethod
    def get_sensors(value: int) -> tuple[Self]:
        """Gets all..."""
        sensors = ()

        for sensor in MultiWiiSensor:
            if sensor | value:
                sensors += (sensor,)

        return sensors
