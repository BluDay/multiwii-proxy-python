#! /usr/bin/env python3

from os     import system
from serial import Serial
from time   import sleep, time

from WiiProxy import MultiWii, Commands, Priority

# -----------------------------------------------------------

serial = Serial("/dev/ttyUSB0", 115200)

sleep(6)

Commands.seed()

fc = MultiWii(serial)

# -----------------------------------------------------------

def arm():
    command = Commands.SET_RAW_RC
    values  = (0, 0, 2000, 1000, 0, 0, 0, 0)
    
    start   = time()
    elapsed = 0

    while elapsed < 0.5:
        fc.execute(command, values)

        sleep(0.05)

        elapsed = time() - start

# -----------------------------------------------------------

fc.start()

print("Arming...")

arm()

print("Armed.")

Commands.IDENT.priority = Priority.Low

for index in range(1000):
    ident       = fc.data[Commands.IDENT]
    status      = fc.data[Commands.STATUS]
    rc          = fc.data[Commands.RC]
    imu         = fc.data[Commands.RAW_IMU]
    attitude    = fc.data[Commands.ATTITUDE]

    print("IDENT                                ")
    print("-------------------------------------")
    print(f"version       = {ident.version}     ")
    print( "multitype     = %s" % ident.multitype)
    print(f"capabilities  = {ident.capabilities}")
    print(f"navi_version  = {ident.navi_version}")
    
    print()

    print("STATUS                               ")
    print("-------------------------------------")
    print(f"cycle_time   = {status.cycle_time}  ")
    print(f"i2c_errors   = {status.i2c_errors}  ")
    print(f"sensors      = {status.sensors}     ")
    print(f"flag         = {status.flag}        ")
    print(f"global_conf  = {status.global_conf} ")

    print()

    print("RC                        ")
    print("--------------------------")
    print(f"roll      = {rc.roll}    ")
    print(f"pitch     = {rc.pitch}   ")
    print(f"yaw       = {rc.yaw}     ")
    print(f"throttle  = {rc.throttle}")
    print(f"aux       = {rc.aux}     ")

    print()

    print("IMU                ")
    print("-------------------")
    print(f"acc   = {imu.acc} ")
    print(f"gyro  = {imu.gyro}")
    print(f"mag   = {imu.mag} ")

    print()

    print("ATTITUDE                      ")
    print("------------------------------")
    print(f"angle    = {attitude.angle}  ")
    print(f"heading  = {attitude.heading}")

    sleep(0.05)

    system("clear") # system("cls")

fc.stop()

print("Exiting...")
