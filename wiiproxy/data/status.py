from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.STATUS)
@MultiWiiDataStructure.struct_format('3HIB')
class Status(MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""

    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int
