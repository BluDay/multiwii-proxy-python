from enum   import IntEnum, unique
from typing import Self

@unique
class MultiWiiSensor(IntEnum):
    """Enumeration of sensor types supported by MultiWii.

    These sensor types indicate the various sensors that can be used with the
    MultiWii flight controller to provide additional data and functionality.
    """
    Acc   = 0
    Baro  = 1
    Mag   = 2
    Gps   = 3
    Sonar = 4

    @classmethod
    def get_sensors(cls, value: int) -> tuple[Self]:
        """Gets all sensors enabled from an integer value.

        This method identifies which sensors are active by performing a
        bitwise OR operation with each sensor type.
        """
        sensors = ()

        for sensor in cls:
            if sensor | value:
                sensors += (sensor,)

        return sensors
