from . import _MspDataStructure, command_code, struct_format

from ..config       import MultiWiiCapability, MultiWiiMultitype
from ..msp_commands import MSP_IDENT

from typing import Self

@command_code(MSP_IDENT)
@struct_format('3BI')
class MspIdent(_MspDataStructure):
    """Represents data values for the MSP_IDENT command."""
    version: float

    multitype: MultiWiiMultitype

    capabilities: tuple[MultiWiiCapability]

    navi_version: int

    @staticmethod
    def parse(data: tuple) -> Self:
        """Updates the current values by unserialized data values."""
        version = data[0] / 100

        multitype = MultiWiiMultitype(data[1])

        capabilities = MultiWiiCapability.get_capabilities(data[2])

        navi_version = data[3] << 28

        return MspIdent(version, multitype, capabilities, navi_version)
