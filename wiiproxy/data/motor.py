from dataclasses import dataclass
from typing      import Self

@dataclass
class MspMotor:
    """Represents data values for the MSP_MOTOR command.

    This class encapsulates the motor speed values for up to eight motors in a
    MultiWii flight controller. Each motor's speed is represented as an integer
    value.

    Attributes
    ----------
    motor 1: int
        The speed value for motor 1.
    motor 2: int
        The speed value for motor 2.
    motor 3: int
        The speed value for motor 3.
    motor 4: int
        The speed value for motor 4.
    motor 5: int
        The speed value for motor 5.
    motor 6: int
        The speed value for motor 6.
    motor 7: int
        The speed value for motor 7.
    motor 8: int
        The speed value for motor 8.
    """
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
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspMotor` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspMotor
            An instance of the `MspMotor` class populated with the parsed data.
        """
        return cls(*data)

@dataclass
class MspMotorPins:
    """Represents data values for the MSP_MOTOR_PINS command.

    This class extends `MspMotor` to provide the motor pin values for up to eight motors
    in a MultiWii flight controller. Each motor's pin value is represented as an integer
    value.

    Attributes
    ----------
    motor 1: int
        The pin value for motor 1.
    motor 2: int
        The pin value for motor 2.
    motor 3: int
        The pin value for motor 3.
    motor 4: int
        The pin value for motor 4.
    motor 5: int
        The pin value for motor 5.
    motor 6: int
        The pin value for motor 6.
    motor 7: int
        The pin value for motor 7.
    motor 8: int
        The pin value for motor 8.
    """
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
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspMotorPins` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspMotorPins
            An instance of the `MspMotorPins` class populated with the parsed data.
        """
        return cls(*data)
