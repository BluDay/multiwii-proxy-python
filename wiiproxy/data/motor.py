from dataclasses import dataclass

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

@dataclass
class MspMotorPins:
    """Represents data values for the MSP_MOTOR_PINS command."""
    values: tuple[int]
