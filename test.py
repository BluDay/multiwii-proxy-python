#! /usr/bin/python3

# -----------------------------------------------------------

import serial as pyserial

from json       import dumps
from os         import system
from time       import sleep
from WiiProxy   import MultiWii

# -----------------------------------------------------------

controller  = None
serial      = None

# -----------------------------------------------------------

serial = pyserial.Serial()

serial.port             = "/dev/ttyUSB0"
serial.baudrate         = 115200
serial.bytesize         = pyserial.EIGHTBITS
serial.parity           = pyserial.PARITY_NONE
serial.stopbits         = pyserial.STOPBITS_ONE
serial.write_timeout    = 3
serial.xonxoff          = False
serial.rtscts           = False
serial.dsrdtr           = False

serial.open()

sleep(6)

controller = MultiWii(serial)

if not controller: exit()

try:
    print("Arming...")
    
    controller.arm()

    print("Armed.")

    sleep(1)

    tests = {
        "Ident"     : controller.get_ident(),
        "IMU"       : controller.get_imu(False),
        "Channels"  : controller.get_channels(False, True),
        "Motors"    : controller.get_motors(),
        "Altitude"  : controller.get_altitude(),
        "Attitude"  : controller.get_attitude(False),
        "GPS"       : controller.get_gps(False)
    }

    print("")

    for x in tests:
        if len(str(tests[x])) > 32:
            print("%s\n\n%s\n" % (
                x, dumps(tests[x], indent = 4))
            )
        else:
            print("%s\n\n%s\n" % (x, tests[x]))

    sleep(1)

    print("Disarming...")
    
    controller.disarm()
    
    print("Disarmed.")
except KeyboardInterrupt:
    exit()

# -----------------------------------------------------------

serial.close()

serial = None
