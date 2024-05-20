from dataclasses import dataclass
from typing      import Self

@dataclass
class MspMotor:
    """Represents data values for the MSP_MOTOR command."""
    motor1: int
    motor2: int
    motor3: int
    motor4: int
    motor5: int
    motor6: int
    motor7: int
    motor8: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)

@dataclass
class MspMotorPins(MspMotor):
    """Represents data values for the MSP_MOTOR_PINS command."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)
