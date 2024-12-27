from ._command import _MspCommand

from typing import Final

MSP_IDENT: Final[_MspCommand] = _MspCommand(100, '3BI:4:!')
"""_MspCommand: An instance representing the MSP_IDENT (100) command."""

MSP_STATUS: Final[_MspCommand] = _MspCommand(101, '3HIB:5:!')
"""_MspCommand: An instance representing the MSP_STATUS (101) command."""

MSP_RAW_IMU: Final[_MspCommand] = _MspCommand(102, '8h:8:!')
"""_MspCommand: An instance representing the MSP_RAW_IMU (102) command."""

MSP_SERVO: Final[_MspCommand] = _MspCommand(103, '16H:16:!')
"""_MspCommand: An instance representing the MSP_SERVO (103) command."""

MSP_MOTOR: Final[_MspCommand] = _MspCommand(104, '16H:16:!')
"""_MspCommand: An instance representing the MSP_MOTOR (104) command."""

MSP_RC: Final[_MspCommand] = _MspCommand(105, '16H:16:!')
"""_MspCommand: An instance representing the MSP_RC (105) command."""

MSP_RAW_GPS: Final[_MspCommand] = _MspCommand(106, '2B2I3H:7:!')
"""_MspCommand: An instance representing the MSP_RAW_GPS (106) command."""

MSP_COMP_GPS: Final[_MspCommand] = _MspCommand(107, '2HB:3:!')
"""_MspCommand: An instance representing the MSP_COMP_GPS (107) command."""

MSP_ATTITUDE: Final[_MspCommand] = _MspCommand(108, '3h:3:!')
"""_MspCommand: An instance representing the MSP_ATTITUDE (108) command."""

MSP_ALTITUDE: Final[_MspCommand] = _MspCommand(109, 'ih:2:!')
"""_MspCommand: An instance representing the MSP_ALTITUDE (109) command."""

MSP_ANALOG: Final[_MspCommand] = _MspCommand(110, 'B3H:4:!')
"""_MspCommand: An instance representing the MSP_ANALOG (110) command."""

MSP_RC_TUNING: Final[_MspCommand] = _MspCommand(111, '7B:7:!')
"""_MspCommand: An instance representing the MSP_RC_TUNING (111) command."""

MSP_PID: Final[_MspCommand] = _MspCommand(112, '30B:30:!')
"""_MspCommand: An instance representing the MSP_PID (112) command."""

MSP_BOX: Final[_MspCommand] = _MspCommand(113, 'H:1:?')
"""_MspCommand: An instance representing the MSP_BOX (113) command."""

MSP_MISC: Final[_MspCommand] = _MspCommand(114, '6HIH4B:12:!')
"""_MspCommand: An instance representing the MSP_MISC (114) command."""

MSP_MOTOR_PINS: Final[_MspCommand] = _MspCommand(115, '8B:8:!')
"""_MspCommand: An instance representing the MSP_MOTOR_PINS (115) command."""

MSP_BOXNAMES: Final[_MspCommand] = _MspCommand(116, 's:1:?')
"""_MspCommand: An instance representing the MSP_BOXNAMES (116) command."""

MSP_PIDNAMES: Final[_MspCommand] = _MspCommand(117, 's:1:?')
"""_MspCommand: An instance representing the MSP_PIDNAMES (117) command."""

MSP_WP: Final[_MspCommand] = _MspCommand(118, 'B3I2HB:7:!')
"""_MspCommand: An instance representing the MSP_WP (118) command."""

MSP_BOXIDS: Final[_MspCommand] = _MspCommand(119, '3HB:4:?')
"""_MspCommand: An instance representing the MSP_BOXIDS (119) command."""

MSP_SERVO_CONF: Final[_MspCommand] = _MspCommand(120, '3HB'*8 + ':32:!')
"""_MspCommand: An instance representing the MSP_SERVO_CONF (120) command."""

MSP_SET_RAW_RC: Final[_MspCommand] = _MspCommand(200, '16H:16:!')
"""_MspCommand: An instance representing the MSP_SET_RAW_RC (200) command."""

MSP_SET_RAW_GPS: Final[_MspCommand] = _MspCommand(201, '2B2I2H:6:!')
"""_MspCommand: An instance representing the MSP_SET_RAW_GPS (201) command."""

MSP_SET_PID: Final[_MspCommand] = _MspCommand(202, '30B:30:!')
"""_MspCommand: An instance representing the MSP_SET_PID (202) command."""

MSP_SET_BOX: Final[_MspCommand] = _MspCommand(203, 'H:1:?')
"""_MspCommand: An instance representing the MSP_SET_BOX (203) command."""

MSP_SET_RC_TUNING: Final[_MspCommand] = _MspCommand(204, '7B:7:!')
"""_MspCommand: An instance representing the MSP_SET_RC_TUNING (204) command."""

MSP_ACC_CALIBRATION: Final[_MspCommand] = _MspCommand(205)
"""_MspCommand: An instance representing the MSP_ACC_CALIBRATION (205) command."""

MSP_MAG_CALIBRATION: Final[_MspCommand] = _MspCommand(206)
"""_MspCommand: An instance representing the MSP_MAG_CALIBRATION (206) command."""

MSP_SET_MISC: Final[_MspCommand] = _MspCommand(207, '6HIH4B:12:!')
"""_MspCommand: An instance representing the MSP_SET_MISC (207) command."""

MSP_RESET_CONF: Final[_MspCommand] = _MspCommand(208)
"""_MspCommand: An instance representing the MSP_RESET_CONF (208) command."""

MSP_SET_WP: Final[_MspCommand] = _MspCommand(209, 'B3I2HB:7:!')
"""_MspCommand: An instance representing the MSP_SET_WP (209) command."""

MSP_SELECT_SETTING: Final[_MspCommand] = _MspCommand(210, 'B:1:!')
"""_MspCommand: An instance representing the MSP_SELECT_SETTING (210) command."""

MSP_SET_HEAD: Final[_MspCommand] = _MspCommand(211, 'h:1:!')
"""_MspCommand: An instance representing the MSP_SET_HEAD (211) command."""

MSP_SET_SERVO_CONF: Final[_MspCommand] = _MspCommand(212, '3HB'*8 + ':32:!')
"""_MspCommand: An instance representing the MSP_SET_SERVO_CONF (212) command."""

MSP_SET_MOTOR: Final[_MspCommand] = _MspCommand(214, '16H:16:!')
"""_MspCommand: An instance representing the MSP_SET_MOTOR (214) command."""

MSP_BIND: Final[_MspCommand] = _MspCommand(240)
"""_MspCommand: An instance representing the MSP_BIND (240) command."""

MSP_EEPROM_WRITE: Final[_MspCommand] = _MspCommand(250)
"""_MspCommand: An instance representing the MSP_EEPROM_WRITE (250) command."""