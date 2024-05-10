from . import _MspDataStructure, _Point3D, command_code, struct_format

from ..msp_commands import MSP_RAW_IMU

from typing import NoReturn

@command_code(MSP_RAW_IMU)
@struct_format('9h')
class MspRawImu(_MspDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _acc: _Point3D[float]

    _gyro: _Point3D[float]

    _mag: _Point3D[float]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._acc  = None
        self._gyro = None
        self._mag  = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def acc(self) -> _Point3D[float]:
        """Gets the current 3D point value of the accelerometer."""
        return self._acc

    @property
    def gyro(self) -> _Point3D[float]:
        """Gets the current 3D point value of the gyroscope."""
        return self._gyro

    @property
    def mag(self) -> _Point3D[float]:
        """Gets the current 3D point value of the magnetometer."""
        return self._mag

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._acc = data[0:3]

        self._gyro = (
            data[3] / 4.096,
            data[4] / 4.096,
            data[5] / 4.096
        )

        self._mag = data[6:9]
