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

    SET_RAW_RC      = 200
    SET_RAW_GPS     = 201
    SET_WAYPOINT    = 209
    EEPROM_WRITE    = 250

    DATA_MIN_SIZE = 6

    ARM_DELAY       = 0.5
    RC_WRITE_DELAY  = 0.05

    PREAMBLE = [b'$', b'M', b'<']

    # ---------------------------------------------------------------------

    def __init__(self, controller: Serial):
        self._controller = controller

    # ---------------------------------------------------------------------

    def _construct_payload(
        self, 
        code: int, 
        data: list = [], 
        size: int = 0):
        payload = (
            ("<3c", MultiWii.PREAMBLE),
            ("<2B", [size, code]),
            ("<%dH" % len(data), data)
        )

        buf = bytes()
        
        for section in payload:
            buf += pack(section[0], *section[1])

        payload = buf[3:len(buf)]

        checksum = int(payload[1])

        if len(payload) > 0x02:
            checksum = 0
            
            for byte in payload:
                checksum = checksum ^ byte
       
        buf += pack(
            "<{}".format("H" if checksum > 0x100 else "B"), 
            checksum
        )

        return buf
        
    def _destruct_payload(self, payload: list, pattern: str):
        if MultiWii.DATA_MIN_SIZE > len(payload):
            return None
        
        data_start  = 0x05
        data_end    = data_start + payload[3]
        
        buf = payload[data_start:data_end]
        
        return unpack("<%s" % pattern, buf)

    # ---------------------------------------------------------------------

    def _write(self, command: bytes):
        if not self._controller: return
        
        self._controller.write(command)

    def _read(self, exp_byte_size: int = 1):
        exp_byte_size += MultiWii.DATA_MIN_SIZE
       
        self._controller.reset_input_buffer()
        self._controller.reset_output_buffer()
        
        buf = None
        
        while not buf:
            buf = self._controller.read(exp_byte_size)
        
        return buf[:exp_byte_size]

    # ---------------------------------------------------------------------

    def arm(self):
        channels = [1500, 1500, 2000, 1000]
        
        start = time()
        
        elapsed = 0
        
        while elapsed < MultiWii.ARM_DELAY:
            self.set_channels(channels)
            
            sleep(MultiWii.RC_WRITE_DELAY)
            
            elapsed = time() - start

    def disarm(self):
        channels = [1500, 1500, 1000, 1000]
        
        start = time()
        
        elapsed = 0
        
        while elapsed < MultiWii.ARM_DELAY:
            self.set_channels(channels)
            
            sleep(MultiWii.RC_WRITE_DELAY)
            
            elapsed = time() - start

    # ---------------------------------------------------------------------

    def set_channels(self, channels: list):
        if len(channels) < 4: return
        
        command = self._construct_payload(
            MultiWii.SET_RAW_RC, channels, len(channels) * 2
        )
        
        self._write(command)

    def get_channels(self, raw: bool):
        command = self._construct_payload(MultiWii.RC)
        
        self._write(command)
        
        buf = self._read(16)
        
        data = self._destruct_payload(buf, "H" * 8)
        
        if raw: return data
        
        types = (
            "roll", "pitch", "yaw", "throttle",
            "aux1", "aux2", "aux3", "aux4"
        )
        
        values = dict()
        
        for x in range(0, len(types)):
            values[types[x]] = data[x]
        
        return values

    def get_imu(self, raw: bool):
        command = self._construct_payload(MultiWii.IMU)
        
        self._write(command)
        
        buf = self._read(18)
        
        data = self._destruct_payload(buf, "h" * 9)
        
        if raw: return data
        
        value_index = 0
        
        coords = self._get_new_coords()
        
        types = ("acc", "gyr")
        
        values = dict()
        
        for i in range(0, len(types)):
            for j in range(0, len(coords)):
                axis = list(coords.keys())[j]
                
                values[types[i] + axis] = float(data[value_index])
                
                value_index += 1
        
        return values

    def get_ident(self):
        command = self._construct_payload(MultiWii.IDENT)
        
        self._write(command)
        
        buf = self._read(7)
        
        data = self._destruct_payload(buf, "BBIB")
        
        return {
            "multitype" : self._get_multitype(data[1]),
            "version"   : str(data[0] / 100)
        }

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
        return {"x": 0.0, "y": 0.0, "z": 0.0}

