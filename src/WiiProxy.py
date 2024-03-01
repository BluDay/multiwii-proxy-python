# ( 0 _ o )

__author__  = "engineer-99b"

__version__ = "2.0"

# ------------------------------------------------------------------------

from enum       import IntEnum, unique
from queue      import PriorityQueue
from serial     import Serial
from struct     import calcsize, pack, unpack
from time       import sleep
from threading  import Thread

# ------------------------------------------------------------------------

@unique
class Multitype(IntEnum):
    Unidentified    = 0
    Tri             = 1
    QuadP           = 2
    QuadX           = 3
    Bi              = 4
    Gimbal          = 5
    Y6              = 6
    Hex6            = 7
    FlyingWing      = 8
    Y4              = 9
    Hex6X           = 10
    OctoX8          = 11
    OctoflatP       = 12
    OctoflatX       = 13
    Airplane        = 14
    Heli120CCPM     = 15
    Heli90Deg       = 16
    VTail4          = 17
    Hex6H           = 18
    Singlecopter    = 21
    Dualcopter      = 20

@unique
class Capability(IntEnum):
    Bind    = 0b0000001
    Dynbal  = 0b0000010
    Flap    = 0b0000100
    Nav     = 0b0001000
    ExtAux  = 0b0010000

@unique
class Sensor(IntEnum):
    Acc     = 0
    Baro    = 1
    Mag     = 2
    Gps     = 3
    Sonar   = 4

@unique
class BoxType(IntEnum):
    Arm         = 0
    Angle       = 1
    Horizon     = 2
    Baro        = 3
    Vario       = 4
    Mag         = 5
    HeadFree    = 6
    HeadAdj     = 7
    CamStab     = 8
    CamTrig     = 9
    GpsHome     = 10
    GpsHold     = 11
    Passthru    = 12
    Beeper      = 13
    LedMax      = 14
    LedLow      = 15
    LLights     = 16
    Calib       = 17
    Governor    = 18
    OsdSwitch   = 19
    Mission     = 20
    Land        = 21

@unique
class Priority(IntEnum):
    Critical    = 1
    High        = 2
    Normal      = 3
    Low         = 4

# ------------------------------------------------------------------------

class Task:
    def __init__(self,
        priority    : Priority, 
        arguments   : tuple
    ) -> None:
        self.priority   = priority
        self.arguments  = arguments

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

# ------------------------------------------------------------------------

class Command:
    def __init__(self,
        name        : str,
        code        : int,
        format      : str,
        dynamic     : bool,
        priority    : Priority
    ) -> None:
        self.name       = name
        self.code       = code
        self.format     = format
        self.dynamic    = dynamic
        self.priority   = priority

    def __iter__(self) -> iter:
        return iter((
            self.size,
            self.code,
            self.format,
            self.dynamic
        ))

    # --------------------------------------------------------------------

    @property
    def name(self) -> str: return self.__name
    
    @property
    def code(self) -> int: return self.__code

    @property
    def format(self) -> str: return self.__format

    @property
    def dynamic(self) -> bool: return self.__dynamic

    @property
    def priority(self) -> Priority: return self.__priority
    
    @property
    def size(self) -> int: return self.__size
    
    # --------------------------------------------------------------------

    @name.setter
    def name(self, value: str) -> str:
        if type(value) is not str:
            raise TypeError("String value required.")

        self.__name = value
    
    @code.setter
    def code(self, value: int) -> int:
        if type(value) is not int:
            raise TypeError("Integer value required.")

        self.__code = value

    @format.setter
    def format(self, value: str) -> str:
        if type(value) is not str:
            raise TypeError("String value required.")

        self.__format   = value
        self.__size     = calcsize('<' + value)

    @dynamic.setter
    def dynamic(self, value: bool) -> bool:
        if type(value) is not bool:
            raise TypeError("Boolean value required.")

        self.__dynamic = value

    @priority.setter
    def priority(self, value: Priority) -> Priority:
        if value is not None:
            if type(value) is not Priority:
                raise TypeError("Priority or NoneType value required.")

        self.__priority = value

# ------------------------------------------------------------------------

class Commands:
    #                   CODE    FORMAT      DYNAMIC     PRIORITY
    IDENT           =   100,    "3BI",      False,      None
    STATUS          =   101,    "3HIB",     False,      None
    RAW_IMU         =   102,    "9h",       False,      Priority.High
    SERVO           =   103,    "8H",       False,      Priority.Normal
    MOTOR           =   104,    "8H",       False,      Priority.High
    RC              =   105,    "8H",       False,      Priority.Critical
    RAW_GPS         =   106,    "2B2I3H",   False,      None
    COMP_GPS        =   107,    "2HB",      False,      None
    ATTITUDE        =   108,    "3h",       False,      Priority.High
    ALTITUDE        =   109,    "ih",       False,      Priority.High
    ANALOG          =   110,    "B3H",      False,      None
    RC_TUNING       =   111,    "7B",       False,      None
    PID             =   112,    "30B",      False,      None
    BOX             =   113,    "H",        True,       None
    MISC            =   114,    "6HIH4B",   False,      None
    MOTOR_PINS      =   115,    "8B",       False,      None
    BOXNAMES        =   116,    "s",        True,       None
    PIDNAMES        =   117,    "s",        True,       None
    WP              =   118,    "B3I2HB",   False,      None
    BOXIDS          =   119,    "B",        True,       None
    SERVO_CONF      =   120,    "3HB",      True,       None

    SET_RAW_RC      =   200,    "8H",       False,      Priority.Critical
    SET_RAW_GPS     =   201,    "2B2I2H",   False,      None
    SET_PID         =   202,    "30B",      False,      None
    SET_BOX         =   203,    "H",        True,       None
    SET_RC_TUNING   =   204,    "7B",       False,      None
    ACC_CALIBRATION =   205,    "",         False,      None
    MAG_CALIBRATION =   206,    "",         False,      None
    SET_MISC        =   207,    "6HIH4B",   False,      None
    RESET_CONF      =   208,    "",         False,      None
    SET_HEAD        =   211,    "h",        False,      None
    SET_SERVO_CONF  =   212,    "56B",      False,      None
    SET_MOTOR       =   214,    "8H",       False,      None
    BIND            =   240,    "",         False,      None
    EEPROM_WRITE    =   250,    "",         False,      None

    @classmethod
    def all(cls) -> tuple:
        for value in cls.__dict__.values():
            if isinstance(value, Command):
                yield value

    @classmethod
    def seed(cls) -> None:
        for key, value in cls.__dict__.items():
            if isinstance(value, tuple):
                setattr(cls, key, Command(key, *value))

# ------------------------------------------------------------------------

class DataType:
    def __init__(self) -> None:
        self.__raw = ()
    
    @property
    def raw(self) -> tuple: return self.__raw

    def evaluate(self, data: tuple) -> None:
        keys = (
            key for key in self.__dict__
                if key[0] != '_'
        )

        for index, key in enumerate(keys):
            setattr(self, key, data[index])

    def update(self, data: tuple) -> None:
        if data is None: return

        self.__raw = data

        self.evaluate(data)

class DataTypes:
    class Single(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.values = ()

        def evaluate(self, data: tuple) -> None:
            self.values = data

    class Names(Single):
        def __init__(self) -> None:
            super().__init__()

        def evaluate(self, data: tuple) -> None:
            self.values = tuple(data[0].decode().split(';')[:-1])

    # --------------------------------------------------------------------

    class Ident(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.version        = 0
            self.multitype      = Multitype.Unidentified
            self.capabilities   = ()
            self.navi_version   = 0

        def evaluate(self, data: tuple) -> None:
            self.version    = data[0] / 100
            self.multitype  = Multitype(data[1])
            
            self.capabilities = ()

            for capability in Capability:
                if capability & data[3]:
                    self.capabilities += capability,

            self.navi_version = data[3] >> 28

    class Status(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.cycle_time     = 0
            self.i2c_errors     = 0
            self.sensors        = ()
            self.flag           = 0
            self.global_conf    = 0

        def evaluate(self, data: tuple) -> None:
            self.cycle_time = data[0]
            self.i2c_errors = data[1]

            self.sensors = ()

            for sensor in Sensor:
                if sensor | data[2]:
                    self.sensors += sensor,

            self.flag           = data[3]
            self.global_conf    = data[4]

    class RawImu(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.acc    = (0, 0, 0)
            self.gyro   = (0, 0, 0)
            self.mag    = (0, 0, 0)

        def evaluate(self, data: tuple) -> None:
            self.acc    = data[0:3]
            self.gyro   = data[3:6]
            self.mag    = data[6:9]

    class Servo(Single):
        def __init__(self) -> None:
            super().__init__()

    class ServoConf(Single):
        def __init__(self) -> None:
            super().__init__()

        def evaluate(self, data: tuple) -> None:
            self.values = ()

            for index in range(0, len(data), 4):
                conf = data[index:index + 4]

                self.values += conf,

    class Motor(Single):
        def __init__(self) -> None:
            super().__init__()

    class MotorPins(Single):
        def __init__(self) -> None:
            super().__init__()

    class Rc(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.roll        = 0
            self.pitch       = 0
            self.yaw         = 0
            self.throttle    = 0
            self.aux         = (0, 0, 0, 0)
        
        def evaluate(self, data: tuple) -> None:
            self.roll       = data[0]
            self.pitch      = data[1]
            self.yaw        = data[2]
            self.throttle   = data[3]
            self.aux        = data[4:]

    class RcTuning(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.rate                   = 0
            self.expo                   = 0
            self.roll_pitch_rate        = 0
            self.yaw_rate               = 0
            self.dynamic_throttle_pid   = 0
            self.throttle_mid           = 0
            self.throttle_expo          = 0

    class RawGps(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.fix            = 0
            self.satellites     = 0
            self.coordinates    = (0, 0)
            self.altitude       = 0
            self.speed          = 0
            self.ground_course  = 0

        def evaluate(self, data: tuple) -> None:
            self.fix            = data[0]
            self.satellites     = data[1]
            self.coordinates    = data[2:4]
            self.altitude       = data[4]
            self.speed          = data[5]
            self.ground_course  = data[6]

    class CompGps(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.distance_to_home   = 0
            self.direction_to_home  = 0
            self.update             = 0

    class Waypoint(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.number         = 0
            self.position       = (0, 0)
            self.alt_hold       = 0
            self.heading        = 0
            self.time_to_stay   = 0
            self.flag           = 0

        def evaluate(self, data: tuple) -> None:
            self.number         = data[0]
            self.position       = data[1:3]
            self.alt_hold       = data[3]
            self.heading        = data[4]
            self.time_to_stay   = data[5]
            self.flag           = data[6]

    class Attitude(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.angle      = (0, 0)
            self.heading    = 0

        def evaluate(self, data: tuple) -> None:
            self.angle      = data[0:2]
            self.heading    = data[2]

    class Altitude(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.estimation         = 0
            self.pressure_variation = 0

    class Analog(DataType):
        def __init__(self) -> None:
            super().__init__()
            
            self.voltage        = 0
            self.power_meter    = 0 # Unclear
            self.rssi           = 0
            self.amperage       = 0

    class Pid(Single):
        def __init__(self) -> None:
            super().__init__()

        def evaluate(self, data: tuple) -> None:
            self.values = ()

            for index in range(0, len(data), 3):
                pid = data[index:index + 3]

                self.values += pid,

    class PidNames(Names):
        def __init__(self) -> None:
            super().__init__()

    class Box(Single):
        def __init__(self) -> None:
            super().__init__()

    class BoxNames(Names):
        def __init__(self) -> None:
            super().__init__()

    class BoxIds(Single):
        def __init__(self) -> None:
            super().__init__()

        def evaluate(self, data: tuple) -> None:
            self.values = ()

            for value in data:
                self.values += BoxType(value),

    class Misc(DataType):
        def __init__(self) -> None:
            super().__init__()

            self.power_trigger      = 0
            self.throttle_idle      = 0
            self.throttle_min       = 0
            self.throttle_max       = 0
            self.throttle_failsafe  = 0
            self.plog_arm           = 0
            self.plog_lifetime      = 0
            self.mag_declination    = 0
            self.battery_scale      = 0
            self.battery_warn_1     = 0
            self.battery_warn_2     = 0
            self.battery_critical   = 0

# ------------------------------------------------------------------------

class MultiWii:
    __PREAMBLE  = 0x24, 0x4d  # $, M
    __ERROR     = 0x21        # !
    __OUT       = 0x3e        # >
    __IN        = 0x3c        # <

    __FMT_PREAMBLE  = "<3b"     # Preamble, Direction
    __FMT_PAYLOAD   = "<2B%s"   # Size, Code, Data[]
    __FMT_CRC       = "<B"      # CRC

    __FMT_BASE = (  __FMT_PREAMBLE       +
                    __FMT_PAYLOAD   [1:] +
                    __FMT_CRC       [1:]    )

    __PREAMBLE_IN = pack(__FMT_PREAMBLE, *__PREAMBLE, __IN)

    __MAX_QUEUE_LENGTH = 100

    __WRITE_DELAY = 0.005

    # --------------------------------------------------------------------

    def __init__(self, serial: Serial) -> None:
        self.__active = False

        self.__data = {
            Commands.IDENT      : DataTypes.Ident(),
            Commands.STATUS     : DataTypes.Status(),
            Commands.RAW_IMU    : DataTypes.RawImu(),
            Commands.SERVO      : DataTypes.Servo(),
            Commands.SERVO_CONF : DataTypes.ServoConf(),
            Commands.MOTOR      : DataTypes.Motor(),
            Commands.MOTOR_PINS : DataTypes.MotorPins(),
            Commands.RC         : DataTypes.Rc(),
            Commands.RC_TUNING  : DataTypes.RcTuning(),
            Commands.ATTITUDE   : DataTypes.Attitude(),
            Commands.ALTITUDE   : DataTypes.Altitude(),
            Commands.RAW_GPS    : DataTypes.RawGps(),
            Commands.COMP_GPS   : DataTypes.CompGps(),
            Commands.WP         : DataTypes.Waypoint(),
            Commands.ANALOG     : DataTypes.Analog(),
            Commands.PID        : DataTypes.Pid(),
            Commands.PIDNAMES   : DataTypes.PidNames(),
            Commands.BOX        : DataTypes.Box(),
            Commands.BOXNAMES   : DataTypes.BoxNames(),
            Commands.BOXIDS     : DataTypes.BoxIds(),
            Commands.MISC       : DataTypes.Misc()
        }

        self.__queue = PriorityQueue(self.__MAX_QUEUE_LENGTH)

        self.__serial = serial

        self.__worker = Thread(target = self.__work)

        self.__write_delay = self.__WRITE_DELAY

    def __del__(self) -> None:
        if self.__active: self.__stop()

    # --------------------------------------------------------------------

    @property
    def active(self) -> bool: return self.__active

    @property
    def data(self) -> dict: return self.__data

    @property
    def write_delay(self) -> float: return self.__WRITE_DELAY

    # --------------------------------------------------------------------

    @write_delay.setter
    def write_delay(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Float value required.")

        if value < 0:
            raise ValueError("Unsigned value required.")
            
        self.__write_delay = value
    
    # --------------------------------------------------------------------

    @classmethod
    def __assemble(cls, format: str, payload: tuple) -> bytes:
        payload = pack(cls.__FMT_PAYLOAD % format, *payload)

        checksum = pack(cls.__FMT_CRC, cls.__crc(payload))

        return cls.__PREAMBLE_IN + payload + checksum

    @classmethod
    def __disassemble(cls, format: str, message: bytes) -> tuple:
        return unpack(cls.__FMT_BASE % format, message)

    @staticmethod
    def __crc(payload: bytes) -> int:
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum

    @staticmethod
    def __dynamic_format(format: str, size: int) -> str:
        if len(format) < 2:
            return str(size) + format

        return format * size

    # --------------------------------------------------------------------

    def __work(self) -> None:
        if not self.__serial: return

        while self.__active:
            if self.__queue.empty():
                for command in self.__data:
                    if command.priority:
                        self.__enqueue(command, ())

            task = self.__dequeue()

            command, data = task.arguments

            self.__flush()

            self.__write(command, data)

            if data: continue

            new_data = self.__read(command)

            if not new_data: continue

            self.__data[command].update(new_data)

            self.__queue.task_done()

    # --------------------------------------------------------------------

    def __enqueue(self, command: Command, data: tuple) -> None:
        if not self.__queue: return

        if self.__queue.full(): return

        priority    = command.priority
        arguments   = (command, data)

        task = Task(priority, arguments)

        self.__queue.put(task)

    def __dequeue(self) -> tuple:
        if not self.__queue: return None

        return self.__queue.get()

    # --------------------------------------------------------------------

    def __write(self, command: Command, data: tuple) -> None:
        if not self.__serial: return

        size, code, format, dynamic = command

        if not data:
            size    = 0
            format  = ""

        if dynamic and data:
            size    = size ** 2
            format  = self.__dynamic_format(format, size)

        payload = (size, code, *data)

        buffer = self.__assemble(format, payload)

        self.__serial.write(buffer)

        sleep(self.__write_delay)

    def __read(self, command: Command) -> tuple:
        if not self.__serial: return None

        size, code, format, dynamic = command

        buffer = self.__serial.read(3)

        if buffer[2] == self.__ERROR:
            return None

        buffer += self.__serial.read(2)

        if buffer[4] != code:
            return None

        data_size = buffer[3]

        buffer += self.__serial.read(data_size)
        buffer += self.__serial.read(1)

        payload     = buffer[3:-1]
        checksum    = buffer[-1]

        if checksum != self.__crc(payload):
            return None

        if dynamic:
            size    = data_size // size
            format  = self.__dynamic_format(format, size)

        message = self.__disassemble(format, buffer)

        if not message:
            return None

        return message[5:-1]

    def __flush(self) -> None:
        if not self.__serial: return

        self.__serial.reset_input_buffer()
        self.__serial.reset_output_buffer()

    # --------------------------------------------------------------------

    def execute(self, command: Command, data: tuple) -> None:
        if not self.__active: return

        if type(command)    is not Command  : return
        if type(data)       is not tuple    : return

        if not command.priority: return

        self.__enqueue(command, data)

    # --------------------------------------------------------------------

    def start(self) -> None:
        if self.__active: return
        
        if not self.__serial.is_open:
            self.__serial.open()

        self.__active = True

        self.__worker.start()

    def stop(self) -> None:
        if not self.__active: return

        self.__active = False

        self.__worker.join()

        if self.__serial.is_open:
            self.__serial.close()

