from ._base import MultiWiiDataStructure

from ..config import MultiWiiCapability, MultiWiiMultitype

from ..messaging.msp_commands import MspCommands

from typing import Final, NoReturn

class Ident(MultiWiiDataStructure):
    """Represents data values for the MSP_IDENT command."""
    
    # ----------------------------------- CLASS CONSTANTS --------------------------------------

    COMMAND_CODE: Final[int] = MspCommands.IDENT

    STRUCT_FORMAT: Final[str] = '3BI'

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

    # --------------------------------------- PROPERTIES ---------------------------------------

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

    def _update(data: tuple[int]) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        self._version = data[0] / 100

        self._multitype = MultiWiiMultitype(data[1])

        capabilities = ()

        for capability in Capability:
            if capability & data[2]:
                capabilities += (capability,)

        self._capabilities = capabilities

        self._navi_version = data[3] << 28
