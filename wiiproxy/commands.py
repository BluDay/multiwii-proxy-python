from .command import Command

from typing import Final

# ------------------------------------ GET COMMANDS ----------------------------------------

MSP_IDENT: Final[Command] = Command(100, '3BI:4:!')
"""Command: An instance representing the MSP_IDENT (100) command."""

MSP_STATUS: Final[Command] = Command(101, '3HIB:5:!')
"""Command: An instance representing the MSP_STATUS (101) command."""

MSP_RAW_IMU: Final[Command] = Command(102, '8h:8:!')
"""Command: An instance representing the MSP_RAW_IMU (102) command."""

MSP_SERVO: Final[Command] = Command(103, '16H:16:!')
"""Command: An instance representing the MSP_SERVO (103) command."""

MSP_MOTOR: Final[Command] = Command(104, '16H:16:!')
"""Command: An instance representing the MSP_MOTOR (104) command."""

MSP_RC: Final[Command] = Command(105, '16H:16:!')
"""Command: An instance representing the MSP_RC (105) command."""

MSP_RAW_GPS: Final[Command] = Command(106, '2B2I3H:7:!')
"""Command: An instance representing the MSP_RAW_GPS (106) command."""

MSP_COMP_GPS: Final[Command] = Command(107, '2HB:3:!')
"""Command: An instance representing the MSP_COMP_GPS (107) command."""

MSP_ATTITUDE: Final[Command] = Command(108, '3h:3:!')
"""Command: An instance representing the MSP_ATTITUDE (108) command."""

MSP_ALTITUDE: Final[Command] = Command(109, 'ih:2:!')
"""Command: An instance representing the MSP_ALTITUDE (109) command."""

MSP_ANALOG: Final[Command] = Command(110, 'B3H:4:!')
"""Command: An instance representing the MSP_ANALOG (110) command."""

MSP_RC_TUNING: Final[Command] = Command(111, '7B:7:!')
"""Command: An instance representing the MSP_RC_TUNING (111) command."""

MSP_PID: Final[Command] = Command(112, '30B:30:!')
"""Command: An instance representing the MSP_PID (112) command."""

MSP_BOX: Final[Command] = Command(113, 'H:1:?')
"""Command: An instance representing the MSP_BOX (113) command."""

MSP_MISC: Final[Command] = Command(114, '6HIH4B:12:!')
"""Command: An instance representing the MSP_MISC (114) command."""

MSP_MOTOR_PINS: Final[Command] = Command(115, '8B:8:!')
"""Command: An instance representing the MSP_MOTOR_PINS (115) command."""

MSP_BOXNAMES: Final[Command] = Command(116, 's:1:?')
"""Command: An instance representing the MSP_BOXNAMES (116) command."""

MSP_PIDNAMES: Final[Command] = Command(117, 's:1:?')
"""Command: An instance representing the MSP_PIDNAMES (117) command."""

MSP_WP: Final[Command] = Command(118, 'B3I2HB:7:!')
"""Command: An instance representing the MSP_WP (118) command."""

MSP_BOXIDS: Final[Command] = Command(119, '3HB:4:?')
"""Command: An instance representing the MSP_BOXIDS (119) command."""

MSP_SERVO_CONF: Final[Command] = Command(120, '3HB'*8 + ':32:!')
"""Command: An instance representing the MSP_SERVO_CONF (120) command."""


# ------------------------------------ SET COMMANDS ----------------------------------------

MSP_SET_RAW_RC: Final[Command] = Command(200, '16H:16:!')
"""Command: An instance representing the MSP_SET_RAW_RC (200) command."""

MSP_SET_RAW_GPS: Final[Command] = Command(201, '2B2I2H:6:!')
"""Command: An instance representing the MSP_SET_RAW_GPS (201) command."""

MSP_SET_PID: Final[Command] = Command(202, '30B:30:!')
"""Command: An instance representing the MSP_SET_PID (202) command."""

MSP_SET_BOX: Final[Command] = Command(203, 'H:1:?')
"""Command: An instance representing the MSP_SET_BOX (203) command."""

MSP_SET_RC_TUNING: Final[Command] = Command(204, '7B:7:!')
"""Command: An instance representing the MSP_SET_RC_TUNING (204) command."""

MSP_ACC_CALIBRATION: Final[Command] = Command(205)
"""Command: An instance representing the MSP_ACC_CALIBRATION (205) command."""

MSP_MAG_CALIBRATION: Final[Command] = Command(206)
"""Command: An instance representing the MSP_MAG_CALIBRATION (206) command."""

MSP_SET_MISC: Final[Command] = Command(207, '6HIH4B:12:!')
"""Command: An instance representing the MSP_SET_MISC (207) command."""

MSP_RESET_CONF: Final[Command] = Command(208)
"""Command: An instance representing the MSP_RESET_CONF (208) command."""

MSP_SET_WP: Final[Command] = Command(209, 'B3I2HB:7:!')
"""Command: An instance representing the MSP_SET_WP (209) command."""

MSP_SELECT_SETTING: Final[Command] = Command(210, 'B:1:!')
"""Command: An instance representing the MSP_SELECT_SETTING (210) command."""

MSP_SET_HEAD: Final[Command] = Command(211, 'h:1:!')
"""Command: An instance representing the MSP_SET_HEAD (211) command."""

MSP_SET_SERVO_CONF: Final[Command] = Command(212, '3HB'*8 + ':32:!')
"""Command: An instance representing the MSP_SET_SERVO_CONF (212) command."""

MSP_SET_MOTOR: Final[Command] = Command(214, '16H:16:!')
"""Command: An instance representing the MSP_SET_MOTOR (214) command."""

MSP_BIND: Final[Command] = Command(240)
"""Command: An instance representing the MSP_BIND (240) command."""

MSP_EEPROM_WRITE: Final[Command] = Command(250)
"""Command: An instance representing the MSP_EEPROM_WRITE (250) command."""
