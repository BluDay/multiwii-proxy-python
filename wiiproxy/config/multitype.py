from enum import IntEnum, unique

@unique
class MultiWiiMultitype(IntEnum):
    """Enumeration of vehicle configurations available in MultiWii.

    These configurations represents different types of aircraft or vehicle setups
    that the flight controller can be configured to control.
    """
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
