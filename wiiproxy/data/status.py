from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.STATUS)
@struct_format('3HIB')
class Status(MultiWiiData):
    """Represents data values for the MSP_STATUS command."""

    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int
