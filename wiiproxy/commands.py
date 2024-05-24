from .command import Command

from typing import Final

# ------------------------------------ GET COMMANDS ----------------------------------------

MSP_IDENT:      Final[Command] = Command(100, '3BI:4:!')
MSP_STATUS:     Final[Command] = Command(101, '3HIB:5:!')
MSP_RAW_IMU:    Final[Command] = Command(102, '8h:8:!')
MSP_SERVO:      Final[Command] = Command(103, '16H:16:!')
MSP_MOTOR:      Final[Command] = Command(104, '16H:16:!')
MSP_RC:         Final[Command] = Command(105, '16H:16:!')
MSP_RAW_GPS:    Final[Command] = Command(106, '2B2I3H:7:!')
MSP_COMP_GPS:   Final[Command] = Command(107, '2HB:3:!')
MSP_ATTITUDE:   Final[Command] = Command(108, '3h:3:!')
MSP_ALTITUDE:   Final[Command] = Command(109, 'ih:2:!')
MSP_ANALOG:     Final[Command] = Command(110, 'B3H:4:!')
MSP_RC_TUNING:  Final[Command] = Command(111, '7B:7:!')
MSP_PID:        Final[Command] = Command(112, '30B:30:!')
MSP_BOX:        Final[Command] = Command(113, 'H:1:?')
MSP_MISC:       Final[Command] = Command(114, '6HIH4B:12:!')
MSP_MOTOR_PINS: Final[Command] = Command(115, '8B:8:!')
MSP_BOXNAMES:   Final[Command] = Command(116, 's:1:?')
MSP_PIDNAMES:   Final[Command] = Command(117, 's:1:?')
MSP_WP:         Final[Command] = Command(118, 'B3I2HB:7:!')
MSP_BOXIDS:     Final[Command] = Command(119, '3HB:4:?')
MSP_SERVO_CONF: Final[Command] = Command(120, '3HB'*8 + ':32:!')

# ------------------------------------ SET COMMANDS ----------------------------------------

MSP_SET_RAW_RC:      Final[Command] = Command(200, '16H:16:!')
MSP_SET_RAW_GPS:     Final[Command] = Command(201, '2B2I2H:6:!')
MSP_SET_PID:         Final[Command] = Command(202, '30B:30:!')
MSP_SET_BOX:         Final[Command] = Command(203, 'H:1:?')
MSP_SET_RC_TUNING:   Final[Command] = Command(204, '7B:7:!')
MSP_ACC_CALIBRATION: Final[Command] = Command(205)
MSP_MAG_CALIBRATION: Final[Command] = Command(206)
MSP_SET_MISC:        Final[Command] = Command(207, '6HIH4B:12:!')
MSP_RESET_CONF:      Final[Command] = Command(208)
MSP_SET_WP:          Final[Command] = Command(209, 'B3I2HB:7:!')
MSP_SELECT_SETTING:  Final[Command] = Command(210, 'B:1:!')
MSP_SET_HEAD:        Final[Command] = Command(211, 'h:1:!')
MSP_SET_SERVO_CONF:  Final[Command] = Command(212, '3HB'*8 + ':32:!')
MSP_SET_MOTOR:       Final[Command] = Command(214, '16H:16:!')
MSP_BIND:            Final[Command] = Command(240)
MSP_EEPROM_WRITE:    Final[Command] = Command(250)
