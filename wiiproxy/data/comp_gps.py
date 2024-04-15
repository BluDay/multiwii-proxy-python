from ._base import command_code, struct_format, MultiWiiData

from ..messaging.msp_commands import MspCommands

@command_code(MspCommands.COMP_GPS)
@struct_format('2HB')
class CompGps(MultiWiiData):
    """Represents data values for the MSP_COMP_GPS command."""

    distance_to_home: int

    direction_to_home: int

    update: int # What?
