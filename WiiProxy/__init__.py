#! /usr/bin/python3

"""---------------------------------------------------+
|   __        ___ _   ____                            |
|   \ \      / (_|_) |  _ \ _ __ _____  ___   _       |
|    \ \ /\ / /| | | | |_) | '__/ _ \ \/ / | | |      |
|     \ V  V / | | | |  __/| | | (_) >  <| |_| |      |
|      \_/\_/  |_|_| |_|   |_|  \___/_/\_\\__, |      |
|                                         |___/ 1.0   |
|                                                     |
|                MADE BY engineer-186f                |
|                                                     |
|            MultiWii Flight Controller <3            |
|                                                     |
|                    FOR Python 3                     |
|                                                     |
+---------------------------------------------------"""

# -------------------------------------------------------------------------

from enum       import IntEnum, unique
from serial     import Serial
from struct     import pack, unpack
from time       import time, sleep

# -------------------------------------------------------------------------

class MultiWii(object):
    @unique
    class Multitype(IntEnum):
        Tri         = 1,
        QuadX       = 3,
        Hex6        = 7,
        Hex6X       = 10,
        OctoX8      = 11,
        OctoFlatP   = 12,
        OctoFlatX   = 13
        
        def __str__(self): 
            return self.name
    
    # ---------------------------------------------------------------------
    
    IDENT       = 100
    IMU         = 102
    SERVO       = 103
    MOTOR       = 104
    RC          = 105
    GPS         = 106
    ATTITUDE    = 108
    ALTITUDE    = 109
    MISC        = 114
    WAYPOINT    = 118
    SERVO_CONF  = 120
    
    SET_RC              = 200
    SET_GPS             = 201
    ACC_CALIBRATION     = 205
    MAG_CALIBRATION     = 206
    RESET_CONF          = 208
    SET_SERVO_CONF      = 212
    SET_MOTOR           = 214
    BIND                = 240
    EEPROM_WRITE        = 250
    
    INIT_TIMEOUT = 3
    
    ARM_DELAY   = 0.5
    WRITE_DELAY = 0.05
    
    PREAMBLE = (0x24, 0x4d)
    
    HEADER_OUTGOING = (*PREAMBLE, 0x3c)
    HEADER_INCOMING = (*PREAMBLE, 0x3e)
    
    OP_DICT_DATA = {
        "attitude"  : ("angx", "angy", "heading"),
        "channels"  : ("roll", "pitch", "throttle", "yaw"),
        "gps"       : ("lat", "lon", "attitude", "speed"),
        "imu"       : ("acc", "gyr", "mag")
    }
    
    # ---------------------------------------------------------------------

    def __init__(self, controller: Serial, standalone: bool = False):
        self.standalone = standalone
        
        self._controller = controller
        
        sleep(MultiWii.INIT_TIMEOUT)

    # ---------------------------------------------------------------------

    def _construct_payload(self, 
        code: int, 
        size: int   = 0, 
        data: list  = []
    ):
        payload = bytes()
        
        data = (
            ("<3b", MultiWii.HEADER_OUTGOING),
            ("<BB", (size, code)),
            ("<%dH" % len(data), data)
        )
        
        for section in data:
            payload += pack(section[0], *section[1])
        
        data = payload[3:]
        
        checksum = code
        
        if len(data) > 0x02:
            checksum = 0
            
            for byte in data:
                checksum ^= byte
        
        payload += pack(
            "<%s" % "H" if checksum > 0xff else "B", 
            checksum
        )
        
        return payload
        
    def _destruct_payload(self, payload: list, pattern: str):
        if not payload: return None
        
        return list(unpack("<%s" % pattern, payload))

    # ---------------------------------------------------------------------

    def _write(self, command: bytes):
        if self._controller: 
            self._controller.write(command)
            
            sleep(MultiWii.WRITE_DELAY)

    def _read(self, size: int = 1):
        header = tuple(self._controller.read(5)[:3])
        
        if header == MultiWii.HEADER_INCOMING:
            payload = self._controller.read(size)
            
            self._controller.read(1)
            
            return payload

    def _write_read(self, code: int, size: int, pattern: str):
        command = self._construct_payload(code)
        
        self._write(command)

        payload = self._read(size)

        return self._destruct_payload(payload, pattern)

    def _flush(self):
        if not self._controller: return
        
        self._controller.reset_input_buffer()
        self._controller.reset_output_buffer()

    # ---------------------------------------------------------------------

    def arm(self):
        channels = [1500, 1500, 2000, 1000]
        
        start = time()
        
        elapsed = 0
        
        while elapsed < MultiWii.ARM_DELAY:
            self.set_channels(channels)
            
            sleep(MultiWii.WRITE_DELAY)
            
            elapsed = time() - start

    def disarm(self):
        channels = [1500, 1500, 1000, 1000]
        
        start = time()
        
        elapsed = 0
        
        while elapsed < MultiWii.ARM_DELAY:
            self.set_channels(channels)
            
            sleep(MultiWii.WRITE_DELAY)
            
            elapsed = time() - start

    # ---------------------------------------------------------------------
    
    def get_servos(self):
        data = self._write_read(MultiWii.SERVO, 16, "8H")
        
        if not data: return None
        
        return data

    def set_motors(self, values: list):
        if len(values) < 0x04: return
        
        command = self._construct_payload(
            MultiWii.SET_MOTOR, len(values) * 2, values
        )
        
        self._write(command)

    def get_motors(self):
        data = self._write_read(MultiWii.MOTOR, 16, "8H")
        
        if not data: return None
        
        return data

    def set_channels(self, values: list):
        if len(values) < 0x04: return
        
        command = self._construct_payload(
            MultiWii.SET_RC, len(values) * 2, values
        )
        
        self._write(command)

    def get_channels(self, 
        raw:            bool = False, 
        include_aux:    bool = False, 
        extra_aux:      bool = False
    ):
        data_sizes = (16, "8H")

        if include_aux and extra_aux:
            data_sizes = (32, "16H")

        data = self._write_read(MultiWii.RC, *data_sizes)
        
        if not data: return None

        if raw:
            if not include_aux: return data[:4]
            
            return data
        
        return self._get_channel_data(data, include_aux)
    
    def get_altitude(self):
        return self._write_read(MultiWii.ALTITUDE, 6, "ih")

    def get_attitude(self, raw: bool = False):
        data = self._write_read(MultiWii.ATTITUDE, 6, "3h")
        
        if not data: return None
        
        if raw: return data
        
        return self._get_attitude_data(data)
            
    def set_gps(self, coordinates: list, attitude: int, speed: int):
        if len(coordinates) < 0x02: return
        
        values = [1, 0] + coordinates + [attitude, speed]
        
        command = self._construct_payload(MultiWii.SET_GPS, 14, values)
        
        self._write(command)
    
    def get_gps(self, raw: bool = False):
        data = self._write_read(MultiWii.GPS, 16, "BBII3H")
        
        if not data: return None
        
        if raw: return data
        
        return self._get_gps_data(data)
    
    def get_imu(self, raw: bool = False):
        data = self._write_read(MultiWii.IMU, 18, "9h")
        
        if not data: return None
        
        if raw: return data
        
        return self._get_imu_data(data)
    
    def get_ident(self, raw: bool = False):
        data = self._write_read(MultiWii.IDENT, 7, "BBIB")
        
        if not data: return None
        
        if raw: return data

        return self._get_ident_data(data)
    
    def set_servo_conf(self, values: list):
        command = self._construct_payload(
            MultiWii.SET_SERVO_CONF, 56, values
        )
        
        self._write(command)
    
    def get_servo_conf(self):
        data = self._write_read(MultiWii.SERVO_CONF, 56, 8 * "3HB")
        
        if not data: return None
        
        if raw: return data
        
        return self._get_servo_conf_data(data)
    
    def get_misc(self, raw: bool = False):
        data = self._write_read(MultiWii.MISC, 19, "6HBH4B")
        
        if not data: return None
        
        if raw: return data 
        
        return self._get_misc_data(data)
    
    def calibrate_acc(self):
        command = self._construct_payload(MultiWii.ACC_CALIBRATION)
        
        self._write(command)
    
    def calibrate_mag(self):
        command = self._construct_payload(MultiWii.MAG_CALIBRATION)
        
        self._write(command)
    
    def set_eeprom(self):
        command = self._construct_payload(MultiWii.EEPROM_WRITE)
        
        self._write(command)
    
    def reset_configuration(self):
        command = self._construct_payload(MultiWii.RESET_CONF)
        
        self._write(command)
    
    def bind_spektrum_satellite(self):
        command = self._construct_payload(MultiWii.BIND)
        
        self._write(command)
    
    # ---------------------------------------------------------------------
    
    def _get_new_coords(self): return { "x": 0.0, "y": 0.0, "z": 0.0 }
    
    def _get_ident_data(self, data: list):
        if len(data) < 0x02: return None
        
        return {
            "multitype" : str(MultiWii.Multitype(data[1])),
            "version"   : str(data[0] / 100)
        }

    def _get_misc_data(self, data: list):
        if len(data) < 0x01: return None
        
        data[7]     /= 10.0
        data[9]     /= 10.0
        data[10]    /= 10.0
        data[11]    /= 10.0

        return { "misc": data }
    
    def _get_servo_conf_data(self, data: list):
        if len(data) < 0x08: return None
        
        values = dict()
        
        for x in range(0, len(data), 4):
            servo = data[x:x + 4]
            
            values["servo%d" % (x / 4)] = {
                "min"       : servo[0],
                "max"       : servo[1],
                "middle"    : servo[2],
                "rate"      : servo[3]
            }
        
        return values

    def _get_channel_data(self, data: list, include_aux: bool):
        if len(data) < 0x04: return None
        
        types = MultiWii.OP_DICT_DATA["channels"]
            
        if self.standalone:
            types[2], types[3] = types[3], types[2]
        
        if include_aux:
            for x in range(0, len(data[4:])):
                types += ("aux%d" % (x + 1),)
        
        values = dict()
        
        for x in range(0, len(types)):
            values[types[x]] = data[x]
        
        return values
    
    def _get_attitude_data(self, data: list):
        if len(data) < 0x03: return
       
        data[0] /= 10.0
        data[1] /= 10.0 

        types = MultiWii.OP_DICT_DATA["attitude"]
        
        values = dict()
        
        for x in range(0, len(data)):
            values[types[x]] = data[x]
        
        return values
    
    def _get_imu_data(self, data: list):
        if len(data) < 0x01: return None
        
        value_index = 0
        
        coords = self._get_new_coords()
        
        types = MultiWii.OP_DICT_DATA["imu"]
        
        values = dict()
        
        for i in range(0, len(types)):
            for j in range(0, len(coords)):
                axis = list(coords.keys())[j]
                
                values[types[i] + axis] = float(data[value_index])
                
                value_index += 1
        
        return values

    def _get_gps_data(self, data: list):
        if len(data) < 0x06: return None
      
        data = data[2:] 

        data[0] /= 10000000
        data[1] /= 10000000
        
        types = MultiWii.OP_DICT_DATA["gps"]
        
        values = dict()
        
        for x in range(0, len(types)):
            values[types[x]] = data[x]
        
        return values

