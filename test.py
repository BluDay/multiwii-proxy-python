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

system("clear")

controller = MultiWii(serial)

if not controller: exit()

# ------- PLAYGROUND! Modify this freely -------

try:
    print("Ident")
    print(controller.get_ident())

    print("\nIMU")
    print(controller.get_imu(False))

    print("\nChannels")
    print(controller.get_channels(False, True))

    print("\nMotors")
    print(controller.get_motors(False))

    print("\nAltitude")
    print(controller.get_altitude())
    
    print("\nAttitude")
    print(controller.get_attitude(False))
    
    print("\nGPS")
    print(controller.get_gps(False))

    print("")

    """
    ---- Print IMU approximately every 10ms ----"""

    print("Arming the craft")
    
    controller.arm()
    
    print("\nPrinting IMU in 2 seconds...")

    sleep(2)

    while True:
        # Print IDENT before fetching IMU to 
        # experience the speed of WiiProxy.
        #
        # print(controller.get_ident(), end = "\r")
        
        system("clear")

        print(controller.get_imu(False), end = "\r")

        sleep(0.025)
    """"""
except KeyboardInterrupt:
    exit()

# ----------------------------------------------

serial.close()

serial = None
