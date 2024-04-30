from .  import _MultiWiiData, command_code, struct_format, Point3D
from .. import MSP_RAW_IMU

from typing import NoReturn

@command_code(MSP_RAW_IMU)
@struct_format('9h')
class RawImu(_MultiWiiData):
    """Represents data values for the MSP_RAW_IMU command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _acc: Point3D[float]

    _gyro: Point3D[float]

    _mag: Point3D[float]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._acc  = None
        self._gyro = None
        self._mag  = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def acc(self) -> Point3D[float]:
        """Gets the current 3D point value of the accelerometer."""
        return self._acc

    @property
    def gyro(self) -> Point3D[float]:
        """Gets the current 3D point value of the gyroscope."""
        return self._gyro

    @property
    def mag(self) -> Point3D[float]:
        """Gets the current 3D point value of the magnetometer."""
        return self._mag

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        """Updates the current values by the provided unserialized data bytes."""
        pass
