from ._base import MultiWiiDataStructure

class RawImu(MultiWiiDataStructure):
    """Represents data values for the MSP_RAW_IMU command."""

    acc: tuple[int]

    gyro: tuple[int]

    mag: tuple[int]
