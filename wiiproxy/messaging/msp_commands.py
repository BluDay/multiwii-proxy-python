from typing import Final

class MspCommands(object):
    """An enum-like class with all MSP command codes."""

    # Get commands.
    IDENT:      Final[int] = 100
    STATUS:     Final[int] = 101
    RAW_IMU:    Final[int] = 102
    SERVO:      Final[int] = 103
    MOTOR:      Final[int] = 104
    RC:         Final[int] = 105
    RAW_GPS:    Final[int] = 106
    COMP_GPS:   Final[int] = 107
    ATTITUDE:   Final[int] = 108
    ALTITUDE:   Final[int] = 109
    ANALOG:     Final[int] = 110
    RC_TUNING:  Final[int] = 111
    PID:        Final[int] = 112
    BOX:        Final[int] = 113
    MISC:       Final[int] = 114
    MOTOR_PINS: Final[int] = 115
    BOXNAMES:   Final[int] = 116
    PIDNAMES:   Final[int] = 117
    WP:         Final[int] = 118
    BOXIDS:     Final[int] = 119
    SERVO_CONF: Final[int] = 120

    # Set commands.
    SET_RAW_RC:      Final[int] = 200
    SET_RAW_GPS:     Final[int] = 201
    SET_PID:         Final[int] = 202
    SET_BOX:         Final[int] = 203
    SET_RC_TUNING:   Final[int] = 204
    ACC_CALIBRATION: Final[int] = 205
    MAG_CALIBRATION: Final[int] = 206
    SET_MISC:        Final[int] = 207
    RESET_CONF:      Final[int] = 208
    SET_HEAD:        Final[int] = 211
    SET_SERVO_CONF:  Final[int] = 212
    SET_MOTOR:       Final[int] = 214
    BIND:            Final[int] = 240
    EEPROM_WRITE:    Final[int] = 250
