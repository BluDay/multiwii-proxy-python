from .data import *

class _MultiWiiData(object):
    """(Some funny description here haha.)"""

    def _reset_data(self) -> None:
        """Resets all data instances. Defines each field if not already defined."""
        self._ident      = Ident()
        self._status     = Status()
        self._raw_imu    = RawImu()
        self._servo      = Servo()
        self._servo_conf = ServoConf()
        self._motor      = Motor()
        self._motor_pins = MotorPins()
        self._rc         = Rc()
        self._rc_tuning  = RcTuning()
        self._attitude   = Attitude()
        self._altitude   = Altitude()
        self._raw_gps    = RawGps()
        self._comp_gps   = CompGps()
        self._waypoint   = Waypoint()
        self._analog     = Analog()
        self._pid        = Pid()
        self._pidnames   = PidNames()
        self._box        = Box()
        self._boxnames   = BoxNames()
        self._boxids     = BoxIds()
        self._misc       = Misc()

    @property
	def ident(self) -> Ident:
        """Gets the..."""
        return self._ident

    @property
	def status(self) -> Status:
        """Gets the..."""
        return self._status

    @property
	def raw_imu(self) -> RawImu:
        """Gets the..."""
        return self._raw_imu

    @property
	def servo(self) -> Servo:
        """Gets the..."""
        return self._servo

    @property
	def servo_conf(self) -> ServoConf:
        """Gets the..."""
        return self._servo_conf

    @property
	def motor(self) -> Motor:
        """Gets the..."""
        return self._motor

    @property
	def motor_pins(self) -> MotorPins:
        """Gets the..."""
        return self._motor_pins

    @property
	def rc(self) -> Rc:
        """Gets the..."""
        return self._rc

    @property
	def rc_tuning(self) -> RcTuning:
        """Gets the..."""
        return self._rc_tuning

    @property
	def attitude(self) -> Attitude:
        """Gets the..."""
        return self._attitude

    @property
	def altitude(self) -> Altitude:
        """Gets the..."""
        return self._altitude

    @property
	def raw_gps(self) -> RawGps:
        """Gets the..."""
        return self._raw_gps

    @property
	def comp_gps(self) -> CompGps:
        """Gets the..."""
        return self._comp_gps

    @property
	def waypoint(self) -> Waypoint:
        """Gets the..."""
        return self._waypoint

    @property
	def analog(self) -> Analog:
        """Gets the..."""
        return self._analog

    @property
	def pid(self) -> Pid:
        """Gets the..."""
        return self._pid

    @property
	def pidnames(self) -> PidNames:
        """Gets the..."""
        return self._pidnames

    @property
	def box(self) -> Box:
        """Gets the..."""
        return self._box

    @property
	def boxnames(self) -> BoxNames:
        """Gets the..."""
        return self._boxnames

    @property
	def boxids(self) -> BoxIds:
        """Gets the..."""
        return self._boxids

    @property
	def misc(self) -> Misc:
        """Gets the..."""
        return self._misc
