"""( 0 _ o )"""

__author__      = 'BluDay'
__copyrights__  = '© 2024 BluDay'
__credits__     = 'BluDay'
__description__ = 'A user-friendly and multithreaded Python 3 module for controlling MultiWii-based drones.'
__license__     = 'MIT'
__maintainer__  = 'BluDay'
__title__       = 'WiiProxy'
__url__         = 'https://github.com/BluDay/wiiproxy'
__version__     = '1.0'

from .msp_commands import (
    MSP_ALTITUDE,
    MSP_ANALOG,
    MSP_ATTITUDE,
    MSP_BOX,
    MSP_BOXIDS,
    MSP_BOXNAMES,
    MSP_COMP_GPS,
    MSP_IDENT,
    MSP_MISC,
    MSP_MOTOR,
    MSP_MOTOR_PINS,
    MSP_PID,
    MSP_PIDNAMES,
    MSP_RAW_GPS,
    MSP_RAW_IMU,
    MSP_RC,
    MSP_RC_TUNING,
    MSP_SERVO,
    MSP_SERVO_CONF,
    MSP_STATUS,
    MSP_WP,
    MSP_ACC_CALIBRATION,
    MSP_BIND,
    MSP_EEPROM_WRITE,
    MSP_MAG_CALIBRATION,
    MSP_RESET_CONF,
    MSP_SET_BOX,
    MSP_SET_HEAD,
    MSP_SET_MISC,
    MSP_SET_MOTOR,
    MSP_SET_PID,
    MSP_SET_RAW_RC,
    MSP_SET_RAW_GPS,
    MSP_SET_RC_TUNING,
    MSP_SET_SERVO_CONF
)

from ._base import MultiWiiData

from .multiwii import MultiWii
