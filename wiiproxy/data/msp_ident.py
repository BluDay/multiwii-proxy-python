from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_IDENT

from ..config import MultiWiiCapability, MultiWiiMultitype

from typing import Final, NoReturn

@command_code(MSP_IDENT)
@struct_format('3BI')
class MspIdent(_MultiWiiData):
    """Represents data values for the MSP_IDENT command."""
    
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __version: float

    __multitype: MultiWiiMultitype

    __capabilities: tuple[MultiWiiCapability]

    __navi_version: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__version      = None
        self.__multitype    = None
        self.__capabilities = None
        self.__navi_version = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def version(self) -> float:
        """Gets the MultiWii version."""
        return self.__version

    @property
    def multitype(self) -> MultiWiiMultitype:
        """Gets the configured vehicle type."""
        return self.__multitype

    @property
    def capabilities(self) -> tuple[MultiWiiCapability]:
        """Gets configured capabilities."""
        return self.__capabilities

    @property
    def navi_version(self) -> int:
        """Gets the NAVI_VERSION."""
        return self.__navi_version

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        data = self.__raw_data

        self.__version = data[0] / 100

        self.__multitype = MultiWiiMultitype(data[1])

        capabilities = ()

        for capability in Capability:
            if capability & data[2]:
                capabilities += (capability,)

        self.__capabilities = capabilities

        self.__navi_version = data[3] << 28
