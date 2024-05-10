from . import _MspNames, command_code, struct_format

from ..msp_commands import MSP_BOXNAMES

@command_code(MSP_BOXNAMES)
class MspBoxNames(_MspNames):
    """Represents data values for the MSP_BOXNAMES command."""
    pass
