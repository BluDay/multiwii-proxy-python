#! /usr/bin/python3

"""
       WiiProxy - Test script

   Modifiable script for executing 
      operations on your craft.

   https://github.com/engineer-186f

"""

# --------------------------------------------------

import json
import serial as pyserial

from os         import system
from time       import sleep
from WiiProxy   import MultiWii

# --------------------------------------------------

controller  = None
serial      = None

# --------------------------------------------------

serial = pyserial.Serial()

serial.port          = "/dev/ttyUSB0"
serial.baudrate      = 115200
serial.bytesize      = pyserial.EIGHTBITS
serial.parity        = pyserial.PARITY_NONE
serial.stopbits      = pyserial.STOPBITS_ONE
serial.write_timeout = 3
serial.xonxoff       = False
serial.rtscts        = False
serial.dsrdtr        = False

serial.open()

sleep(6)

controller = MultiWii(serial)

if not controller: exit()

# ------- PLAYGROUND! Modify this freely -------

try:
    print("\nIdent")
    print(controller.get_ident())

    print("\nIMU")
    print(controller.get_imu(False))

    print("\nChannels")
    print(controller.get_channels(False))

    print("\nMotors")
    print(controller.get_motors(False))

    print("\nAltitude")
    print(controller.get_altitude())
    
    print("\nAttitude")
    print(controller.get_attitude())

    print("")

    """ 
    print("Arming the craft")
    
    controller.arm()
    
    sleep(3)

    print("Getting current channel values")
    print(controller.get_channels(True))

    print("Printing IMU in 2 seconds...")

    sleep(2)

    while True:
        system("clear")

        print(controller.get_imu(False))

        sleep(0.05)
    """
except KeyboardInterrupt:
    exit()

# ----------------------------------------------

serial.close()

serial = None
