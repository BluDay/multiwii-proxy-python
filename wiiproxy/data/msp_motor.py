from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_MOTOR

from typing import NamedTuple

@command_code(MSP_MOTOR)
@struct_format('8H')
class MspMotor(_MspValues):
    """Represents data values for the MSP_MOTOR command."""
    pass

class MspSetMotor(NamedTuple):
    """Data values as a tuple for the MSP_SET_MOTOR command."""
    motor1: int
    motor2: int
    motor3: int
    motor4: int
    motor5: int
    motor6: int
    motor7: int
    motor8: int
