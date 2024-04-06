from .       import MultiWiiCommand
from .config import PriorityType

class MultiWiiCommands(object):
    """This class contains the info for all of the available MultiWii commands.

    Structure for commands defined below:

        {COMMAND_NAME} = MultiWiiCommand(code, format, is_dynamic, priority_type)
    """

    # Get commands.
    IDENT      = MultiWiiCommand(100, '3BI',    False, PriorityType.Inactive)
    STATUS     = MultiWiiCommand(101, '3HIB',   False, PriorityType.Inactive)
    RAW_IMU    = MultiWiiCommand(102, '9h',     False, PriorityType.High)
    SERVO      = MultiWiiCommand(103, '8H',     False, PriorityType.Normal)
    MOTOR      = MultiWiiCommand(104, '8H',     False, PriorityType.High)
    RC         = MultiWiiCommand(105, '8H',     False, PriorityType.Critical)
    RAW_GPS    = MultiWiiCommand(106, '2B2I3H', False, PriorityType.Inactive)
    COMP_GPS   = MultiWiiCommand(107, '2HB',    False, PriorityType.Inactive)
    ATTITUDE   = MultiWiiCommand(108, '3h',     False, PriorityType.High)
    ALTITUDE   = MultiWiiCommand(109, 'ih',     False, PriorityType.High)
    ANALOG     = MultiWiiCommand(110, 'B3H',    False, PriorityType.Inactive)
    RC_TUNING  = MultiWiiCommand(111, '7B',     False, PriorityType.Inactive)
    PID        = MultiWiiCommand(112, '30B',    False, PriorityType.Inactive)
    BOX        = MultiWiiCommand(113, 'H',      True,  PriorityType.Inactive)
    MISC       = MultiWiiCommand(114, '6HIH4B', False, PriorityType.Inactive)
    MOTOR_PINS = MultiWiiCommand(115, '8B',     False, PriorityType.Inactive)
    BOXNAMES   = MultiWiiCommand(116, 's',      True,  PriorityType.Inactive)
    PIDNAMES   = MultiWiiCommand(117, 's',      True,  PriorityType.Inactive)
    WP         = MultiWiiCommand(118, 'B3I2HB', False, PriorityType.Inactive)
    BOXIDS     = MultiWiiCommand(119, 'B',      True,  PriorityType.Inactive)
    SERVO_CONF = MultiWiiCommand(120, '3HB',    True,  PriorityType.Inactive)
    
    # Set commands.
    SET_RAW_RC      = MultiWiiCommand(200, '8H',     False, PriorityType.Critical)
    SET_RAW_GPS     = MultiWiiCommand(201, '2B2I2H', False, PriorityType.Inactive)
    SET_PID         = MultiWiiCommand(202, '30B',    False, PriorityType.Inactive)
    SET_BOX         = MultiWiiCommand(203, 'H',      True,  PriorityType.Inactive)
    SET_RC_TUNING   = MultiWiiCommand(204, '7B',     False, PriorityType.Inactive)
    ACC_CALIBRATION = MultiWiiCommand(205, '',       False, PriorityType.Inactive)
    MAG_CALIBRATION = MultiWiiCommand(206, '',       False, PriorityType.Inactive)
    SET_MISC        = MultiWiiCommand(207, '6HIH4B', False, PriorityType.Inactive)
    RESET_CONF      = MultiWiiCommand(208, '',       False, PriorityType.Inactive)
    SET_HEAD        = MultiWiiCommand(211, 'h',      False, PriorityType.Inactive)
    SET_SERVO_CONF  = MultiWiiCommand(212, '56B',    False, PriorityType.Inactive)
    SET_MOTOR       = MultiWiiCommand(214, '8H',     False, PriorityType.Inactive)
    BIND            = MultiWiiCommand(240, '',       False, PriorityType.Inactive)
    EEPROM_WRITE    = MultiWiiCommand(250, '',       False, PriorityType.Inactive)
