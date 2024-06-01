from dataclasses import dataclass
from typing      import Self

@dataclass
class MspServo:
    """
    Represents data values for the MSP_SERVO command.

    This class encapsulates the servo values for channels in the MultiWii flight controller.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    values: tuple[int]
    """tuple[int]: The servo output values for each channel."""

    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspServo` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspServo
            An instance of the `MspServo` class populated with the parsed data.
        """
        return cls(*data)

@dataclass
class MspServoConf:
    """
    Represents data values for the MSP_SERVO_CONF command.

    This class encapsulates the servo configuration values for setting up servo endpoints,
    middle points, and rates in the MultiWii flight controller.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    values: tuple[int]
    """tuple[int]: The servo configuration values for each servo channel."""

    # ------------------------------------ CLASS METHODS ---------------------------------------

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns aninstance of
        the `MspServoConf` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspServoConf
            An instance of the `MspServoConf` class populated with the parsed data.
        """
        conf_count = len(data) / 4

        values = ()

        for index in range(conf_count, step=4):
            servo_conf_item = ServoConfItem(
                min=data[index],
                max=data[index + 1],
                middle=data[index + 2],
                rate=data[index + 3]
            )

            values += (servo_conf_item,)

        return cls(values)

@dataclass
class MspServoConfItem:
    """
    Represents data values for the MSP_SET_SERVO_CONF command.

    This class encapsulates the configuration values for a single servo channel in the
    MultiWii flight controller.
    """

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    min: int
    """int: The minimum value for the servo endpoint."""

    max: int
    """int: The maximum value for the servo endpoint."""

    middle: int
    """int: The middle value for the servo endpoint."""

    rate: int
    """int: The rate vlaue for the servo channel."""
