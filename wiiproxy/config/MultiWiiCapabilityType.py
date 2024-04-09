from enum import IntEnum, unique

@unique
class MultiWiiCapabilityType(IntEnum):
    """
    Represents some capabilities that the flight controller has.
    """
    Bind   = 0b0000001
    Dynbal = 0b0000010
    Flap   = 0b0000100
    Nav    = 0b0001000
    ExtAux = 0b0010000
