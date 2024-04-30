from .  import _MultiWiiData, _Point3D, command_code, struct_format
from .. import MSP_RAW_IMU

from typing import NoReturn

@command_code(MSP_RAW_IMU)
@struct_format('9h')
class MspRawImu(_MultiWiiData):
    """Represents data values for the MSP_RAW_IMU command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    __acc: _Point3D[float]

    __gyro: _Point3D[float]

    __mag: _Point3D[float]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self.__acc  = None
        self.__gyro = None
        self.__mag  = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def acc(self) -> _Point3D[float]:
        """Gets the current 3D point value of the accelerometer."""
        return self.__acc

    @property
    def gyro(self) -> _Point3D[float]:
        """Gets the current 3D point value of the gyroscope."""
        return self.__gyro

    @property
    def mag(self) -> _Point3D[float]:
        """Gets the current 3D point value of the magnetometer."""
        return self.__mag

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
