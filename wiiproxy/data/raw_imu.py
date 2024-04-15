from ._base import _MultiWiiDataStructure

class RawImu(_MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""
    acc: tuple[int]

    gyro: tuple[int]

    mag: tuple[int]
