from wiiproxy.data._base import _MultiWiiDataIntegerValues, _MultiWiiDataStringValues

class Pid(_MultiWiiDataIntegerValues):
    """Represents data values for the MSP_PID command."""
    pass

class PidNames(_MultiWiiDataStringValues):
    """Represents data values for the MSP_PIDNAMES command."""
    pass
