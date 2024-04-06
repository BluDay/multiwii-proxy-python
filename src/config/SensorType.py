from enum import IntEnum, unique

@unique
class SensorType(IntEnum):
    """Represents different sensor types."""
    Acc   = 0
    Baro  = 1
    Mag   = 2
    Gps   = 3
    Sonar = 4
