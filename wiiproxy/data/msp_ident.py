from . import _MspDataStructure, command_code, struct_format

from ..config       import MultiWiiCapability, MultiWiiMultitype
from ..msp_commands import MSP_IDENT

from typing import Final, NoReturn

@command_code(MSP_IDENT)
@struct_format('3BI')
class MspIdent(_MspDataStructure):
    """Represents data values for the MSP_IDENT command."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _version: float

    _multitype: MultiWiiMultitype

    _capabilities: tuple[MultiWiiCapability]

    _navi_version: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._version      = None
        self._multitype    = None
        self._capabilities = None
        self._navi_version = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def version(self) -> float:
        """Gets the MultiWii version."""
        return self._version

    @property
    def multitype(self) -> MultiWiiMultitype:
        """Gets the configured vehicle type."""
        return self._multitype

    @property
    def capabilities(self) -> tuple[MultiWiiCapability]:
        """Gets configured capabilities."""
        return self._capabilities

    @property
    def navi_version(self) -> int:
        """Gets the NAVI_VERSION."""
        return self._navi_version

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update_values(self, raw_data: bytes) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        self._version = raw_data[0] / 100

        self._multitype = MultiWiiMultitype(raw_data[1])

        capabilities = ()

        for capability in Capability:
            if capability & raw_data[2]:
                capabilities += (capability,)

        self._capabilities = capabilities

        self._navi_version = raw_data[3] << 28
