from dataclasses import dataclass
from typing      import Self

@dataclass
class MspServo:
    """Represents data values for the MSP_SERVO command."""
    values: tuple[int]

    @classmethod
    def parse(cls, data: tuple) -> Self:
        return cls(*data)

@dataclass
class MspServoConf:
    """Represents data values for the MSP_SERVO_CONF command."""
    values: tuple[int]

    @classmethod
    def parse(cls, data: tuple) -> Self:
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
    """Represents data values for the MSP_SET_SERVO_CONF command."""
    min: int

    max: int

    middle: int

    rate: int
