from typing import Final

class MultiWiiCommands(object):
    """
    An enum-like class with all MSP command codes.
    """

    # Get commands.
    MSP_IDENT:      Final[int] = 100
    MSP_STATUS:     Final[int] = 101
    MSP_RAW_IMU:    Final[int] = 102
    MSP_SERVO:      Final[int] = 103
    MSP_MOTOR:      Final[int] = 104
    MSP_RC:         Final[int] = 105
    MSP_RAW_GPS:    Final[int] = 106
    MSP_COMP_GPS:   Final[int] = 107
    MSP_ATTITUDE:   Final[int] = 108
    MSP_ALTITUDE:   Final[int] = 109
    MSP_ANALOG:     Final[int] = 110
    MSP_RC_TUNING:  Final[int] = 111
    MSP_PID:        Final[int] = 112
    MSP_BOX:        Final[int] = 113
    MSP_MISC:       Final[int] = 114
    MSP_MOTOR_PINS: Final[int] = 115
    MSP_BOXNAMES:   Final[int] = 116
    MSP_PIDNAMES:   Final[int] = 117
    MSP_WP:         Final[int] = 118
    MSP_BOXIDS:     Final[int] = 119
    MSP_SERVO_CONF: Final[int] = 120

    # Set commands.
    MSP_SET_RAW_RC:      Final[int] = 200
    MSP_SET_RAW_GPS:     Final[int] = 201
    MSP_SET_PID:         Final[int] = 202
    MSP_SET_BOX:         Final[int] = 203
    MSP_SET_RC_TUNING:   Final[int] = 204
    MSP_ACC_CALIBRATION: Final[int] = 205
    MSP_MAG_CALIBRATION: Final[int] = 206
    MSP_SET_MISC:        Final[int] = 207
    MSP_RESET_CONF:      Final[int] = 208
    MSP_SET_HEAD:        Final[int] = 211
    MSP_SET_SERVO_CONF:  Final[int] = 212
    MSP_SET_MOTOR:       Final[int] = 214
    MSP_BIND:            Final[int] = 240
    MSP_EEPROM_WRITE:    Final[int] = 250
