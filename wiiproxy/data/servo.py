from dataclasses import dataclass

@dataclass
class MspServo:
    """Represents data values for the MSP_SERVO command."""
    values: tuple[int]

@dataclass
class MspServoConf:
    """Represents data values for the MSP_SERVO_CONF command."""
    values: tuple[int]

@dataclass
class MspServoConfItem:
    """Represents data values for the MSP_SET_SERVO_CONF command."""
    min: int

    max: int

    middle: int

    rate: int
