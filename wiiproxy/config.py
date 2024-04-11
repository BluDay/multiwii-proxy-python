from enum import IntEnum, unique

@unique
class MultiWiiBox(IntEnum):
    """Represents the various boxes that can be checked."""
    Arm       = 0
    Angle     = 1
    Horizon   = 2
    Baro      = 3
    Vario     = 4
    Mag       = 5
    HeadFree  = 6
    HeadAdj   = 7
    CamStab   = 8
    CamTrig   = 9
    GpsHome   = 10
    GpsHold   = 11
    Passthru  = 12
    Beeper    = 13
    LedMax    = 14
    LedLow    = 15
    LLights   = 16
    Calib     = 17
    Governor  = 18
    OsdSwitch = 19
    Mission   = 20
    Land      = 21

@unique
class MultiWiiCapability(IntEnum):
    """Represents some capabilities that the flight controller has."""
    Bind   = 0b0000001
    Dynbal = 0b0000010
    Flap   = 0b0000100
    Nav    = 0b0001000
    ExtAux = 0b0010000

@unique
class MultiWiiMultitype(IntEnum):
    """Represents different types of available vehicle configurations."""
    Unidentified = 0
    Tri          = 1
    QuadP        = 2
    QuadX        = 3
    Bi           = 4
    Gimbal       = 5
    Y6           = 6
    Hex6         = 7
    FlyingWing   = 8
    Y4           = 9
    Hex6X        = 10
    OctoX8       = 11
    OctoflatP    = 12
    OctoflatX    = 13
    Airplane     = 14
    Heli120CCPM  = 15
    Heli90Deg    = 16
    VTail4       = 17
    Hex6H        = 18
    Singlecopter = 21
    Dualcopter   = 20

@unique
class MultiWiiSensor(IntEnum):
    """Represents different sensor types."""
    Acc   = 0
    Baro  = 1
    Mag   = 2
    Gps   = 3
    Sonar = 4
