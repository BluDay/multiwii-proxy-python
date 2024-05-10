from . import _MspValues, command_code, struct_format

from ..msp_commands import MSP_BOX

@command_code(MSP_BOX)
@struct_format('H', has_variable_size=True)
class MspBox(_MspValues):
    """Represents data values for the MSP_BOX command."""
    pass
