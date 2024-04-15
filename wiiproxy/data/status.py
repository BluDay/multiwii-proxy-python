from . import command_code, struct_format, MultiWiiData

from ..messaging import MspCommands

@command_code(MspCommands.STATUS)
@struct_format('3HIB')
class Status(MultiWiiData):
    """Represents data values for the MSP_STATUS command."""

    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int
