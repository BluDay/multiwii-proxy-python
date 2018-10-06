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

from enum       import IntEnum
from serial     import Serial
from struct     import pack, unpack
from time       import time, sleep

# -------------------------------------------------------------------------

class MultiWii(object):
    class Multitype(IntEnum):
        Tri         = 1,
        QuadX       = 3,
        Hex6        = 7,
        Hex6X       = 10,
        OctoX8      = 11,
        OctoFlatP   = 12,
        OctoFlatX   = 13
    
    # ---------------------------------------------------------------------
    
    IDENT       = 100
    IMU         = 102
    MOTOR       = 104
    RC          = 105
    GPS         = 106
    ATTITUDE    = 108
    ALTITUDE    = 109
    WAYPOINT    = 118
    
    SET_RC      = 200
    SET_GPS     = 201
    SET_MOTOR   = 214
    
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
        self._controller    = controller
        self.standalone     = standalone

    # ---------------------------------------------------------------------

    def _construct_payload(self, 
        code: int, 
        size: int = 0, 
        data: list = []
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
                checksum = checksum ^ byte
        
        payload += pack(
            "<%s" % "H" if checksum > 0xff else "B",
            checksum
        )
        
        return payload
        
    def _destruct_payload(self, payload: list, pattern: str):
        if not payload: return None
        
        return unpack("<%s" % pattern, payload)

    # ---------------------------------------------------------------------

    def _write(self, command: bytes):
        if self._controller: self._controller.write(command)

    def _read(self, size: int = 1):
        self._flush()
        
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
    
    def set_motors(self, values: list):
        if len(values) < 0x04: return
        
        command = self._construct_payload(
            MultiWii.SET_MOTOR, len(values) * 2, values
        )
        
        self._write(command)

    def get_motors(self, raw: bool, limit: int = 8):
        if limit < 0x01: return
        
        data = self._write_read(MultiWii.MOTOR, 16, "8H")
        
        if not data: return None

        data = data[:limit]
        
        if raw: return data
        
        return self._get_motor_values(data)

    def set_channels(self, values: list):
        if len(values) < 0x04: return
        
        command = self._construct_payload(
            MultiWii.SET_RC, len(values) * 2, values
        )
        
        self._write(command)

    def get_channels(self, 
        raw:            bool, 
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
        
        return self._get_channel_values(data, include_aux)
    
    def get_altitude(self):
        return self._write_read(MultiWii.ALTITUDE, 6, "ih")

    def get_attitude(self, raw: bool):
        data = self._write_read(MultiWii.ATTITUDE, 6, "3h")
        
        if not data: return None

        if raw: return data
        
        types = MultiWii.OP_DICT_DATA["attitude"]
        
        values = dict()
        
        for x in range(0, len(data)):
            values[types[x]] = data[x]
        
        return values
    
    def set_gps(self, coordinates: list, attitude: int, speed: int):
        if len(coordinates) < 0x02: return
        
        values = [1, 0] + coordinates + [attitude, speed]

        command = self._construct_payload(MultiWii.SET_GPS, 14, values)

        self._write(command)

    def get_gps(self, raw: bool):
        data = self._write_read(MultiWii.GPS, 16, "BBII3H")
        
        if not data: return None

        data = data[2:] 

        data[0] /= 10000000
        data[1] /= 10000000

        if raw: return data

        return self._get_gps_data(data)

    def get_imu(self, raw: bool):
        data = self._write_read(MultiWii.IMU, 18, "9h")
        
        if not data: return None

        if raw: return data
        
        return self._get_imu_data(data)

    def get_ident(self):
        data = self._write_read(MultiWii.IDENT, 7, "BBIB")
        
        if not data: return None

        return self._get_ident_data(data)

    # ---------------------------------------------------------------------

    def _get_multitype(self, index: int):
        try:
            if not MultiWii.Multitype(index):
                return None
            
            multitype = str(MultiWii.Multitype(index))
            
            return multitype.split(".")[1]
        except IndexError:
            return None

    def _get_new_coords(self):
        return { "x": 0.0, "y": 0.0, "z": 0.0 }

    def _get_ident_data(self, data: list):
        if len(data) < 0x02: return None
        
        return {
            "multitype" : self._get_multitype(data[1]),
            "version"   : str(data[0] / 100)
        }

    def _get_motor_values(self, data: list):
        if len(data) < 0x04: return None
        
        values = dict()
        
        for x in range(0, len(data)):
            values[("motor%d" % (x + 1))] = data[x] 
        
        return values

    def _get_channel_values(self, data: list, include_aux: bool):
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
        if len(data) < 0x04: return None
        
        types = MultiWii.OP_DICT_DATA["gps"]
        
        values = dict()
        
        for x in range(0, len(types)):
            values[types[x]] = data[x]
        
        return values

