from ._base import MultiWiiDataStructure

from ..messaging.msp_commands import MspCommands

@MultiWiiDataStructure.command_code(MspCommands.COMP_GPS)
@MultiWiiDataStructure.struct_format('2HB')
class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""

    distance_to_home: int

    direction_to_home: int

    update: int # What?
