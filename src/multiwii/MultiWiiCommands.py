from .       import 
from .config import PriorityType

class MultiWiiCommands(object):
    """
    This class contains the info for all of the available MultiWii commands.

    Structure for commands defined below:

        {COMMAND_NAME} = (code, format, is_dynamic, priority_type)
    """

    # Get commands.
    IDENT      = (100, '3BI',    False, PriorityType.Inactive)
    STATUS     = (101, '3HIB',   False, PriorityType.Inactive)
    RAW_IMU    = (102, '9h',     False, PriorityType.High)
    SERVO      = (103, '8H',     False, PriorityType.Normal)
    MOTOR      = (104, '8H',     False, PriorityType.High)
    RC         = (105, '8H',     False, PriorityType.Critical)
    RAW_GPS    = (106, '2B2I3H', False, PriorityType.Inactive)
    COMP_GPS   = (107, '2HB',    False, PriorityType.Inactive)
    ATTITUDE   = (108, '3h',     False, PriorityType.High)
    ALTITUDE   = (109, 'ih',     False, PriorityType.High)
    ANALOG     = (110, 'B3H',    False, PriorityType.Inactive)
    RC_TUNING  = (111, '7B',     False, PriorityType.Inactive)
    PID        = (112, '30B',    False, PriorityType.Inactive)
    BOX        = (113, 'H',      True,  PriorityType.Inactive)
    MISC       = (114, '6HIH4B', False, PriorityType.Inactive)
    MOTOR_PINS = (115, '8B',     False, PriorityType.Inactive)
    BOXNAMES   = (116, 's',      True,  PriorityType.Inactive)
    PIDNAMES   = (117, 's',      True,  PriorityType.Inactive)
    WP         = (118, 'B3I2HB', False, PriorityType.Inactive)
    BOXIDS     = (119, 'B',      True,  PriorityType.Inactive)
    SERVO_CONF = (120, '3HB',    True,  PriorityType.Inactive)
    
    # Set commands.
    SET_RAW_RC      = (200, '8H',     False, PriorityType.Critical)
    SET_RAW_GPS     = (201, '2B2I2H', False, PriorityType.Inactive)
    SET_PID         = (202, '30B',    False, PriorityType.Inactive)
    SET_BOX         = (203, 'H',      True,  PriorityType.Inactive)
    SET_RC_TUNING   = (204, '7B',     False, PriorityType.Inactive)
    ACC_CALIBRATION = (205, '',       False, PriorityType.Inactive)
    MAG_CALIBRATION = (206, '',       False, PriorityType.Inactive)
    SET_MISC        = (207, '6HIH4B', False, PriorityType.Inactive)
    RESET_CONF      = (208, '',       False, PriorityType.Inactive)
    SET_HEAD        = (211, 'h',      False, PriorityType.Inactive)
    SET_SERVO_CONF  = (212, '56B',    False, PriorityType.Inactive)
    SET_MOTOR       = (214, '8H',     False, PriorityType.Inactive)
    BIND            = (240, '',       False, PriorityType.Inactive)
    EEPROM_WRITE    = (250, '',       False, PriorityType.Inactive)
