from enum import IntEnum, unique

from typing import Self

@unique
class MultiWiiBox(IntEnum):
    """
    Represents the various boxes that can be checked in a MultiWii flight controller.

    Each box corresponds to a specific function or mode that can be activated in the
    flight controller's configuration.
    """
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
class MultiWiiBoxState(IntEnum):
    """
    Represents the state of an auxiliary (aux) control box in MultiWii flight controller.

    The state indicates whether the box is unselected (Empty), or selected at a LOW (Low),
    MID (Mid), or HIGH (High) position.
    """
    Empty = 0b000
    Low   = 0b001
    Mid   = 0b010
    High  = 0b100

    @classmethod
    def parse_value_to_enum(cls, value: int) -> Self:
        """
        Gets a parsed value from the provided integer value.

        Parameters
        ----------
        value : int
            The integer value to evaluate the first three bits from.

        Returns
        -------
        A parsed value or `Empty` if unsuccessful.
        """
        value = value & 0x7

        if value & cls.Low.value:
            return cls.Low

        if value & cls.Mid.value:
            return cls.Mid

        if value & cls.High.value:
            return cls.High

        return cls.Empty

@unique
class MultiWiiCapability(IntEnum):
    """
    Represents various capabilities of a MultiWii flight controller.

    Each capability indicates a specific feature that the flight controller supports.
    """
    Bind   = 0b00001
    Dynbal = 0b00010
    Flap   = 0b00100
    Nav    = 0b01000
    ExtAux = 0b10000

@unique
class MultiWiiMultitype(IntEnum):
    """
    Enumeration of vehicle configurations available in MultiWii.

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

@unique
class MultiWiiSensor(IntEnum):
    """
    Enumeration of sensor types supported by MultiWii.

    These sensor types indicate the various sensors that can be used with the
    MultiWii flight controller to provide additional data and functionality.
    """
    Acc   = 0
    Baro  = 1
    Mag   = 2
    Gps   = 3
    Sonar = 4