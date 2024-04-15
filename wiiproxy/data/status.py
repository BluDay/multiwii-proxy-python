from ._base import _MultiWiiDataStructure

class Status(_MultiWiiDataStructure):
    """Represents data values for the MSP_STATUS command."""
    cycle_time: int

    i2c_errors: int

    sensors: tuple[int]

    flag: int

    global_conf: int
