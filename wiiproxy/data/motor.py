from dataclasses import dataclass
from typing      import Self

@dataclass
class MspMotor:
    """
    Represents data values for the MSP_MOTOR command.

    This class encapsulates the motor speed values for up to eight motors in a MultiWii flight
    controller. Each motor's speed is represented as an integer value.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    motor1: int
    """int: The speed value for motor 1."""

    motor2: int
    """int: The speed value for motor 2."""

    motor3: int
    """int: The speed value for motor 3."""

    motor4: int
    """int: The speed value for motor 4."""

    motor5: int
    """int: The speed value for motor 5."""

    motor6: int
    """int: The speed value for motor 6."""

    motor7: int
    """int: The speed value for motor 7."""

    motor8: int
    """int: The speed value for motor 8."""

    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspMotor` class.

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
    """
    Represents data values for the MSP_MOTOR_PINS command.

    This class extends `MspMotor` to provide the motor pin values for up to eight motors
    in a MultiWii flight controller. Each motor's pin value is represented as an integer
    value.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    motor1: int
    """int: The pin value for motor 1."""

    motor2: int
    """int: The pin value for motor 2."""

    motor3: int
    """int: The pin value for motor 3."""

    motor4: int
    """int: The pin value for motor 4."""

    motor5: int
    """int: The pin value for motor 5."""

    motor6: int
    """int: The pin value for motor 6."""

    motor7: int
    """int: The pin value for motor 7."""

    motor8: int
    """int: The pin value for motor 8."""

    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspMotorPins` class.

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
