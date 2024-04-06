#!/usr/bin/env python3

from os     import system
from serial import Serial
from time   import sleep, time

from .src import WiiProxy, MultiWiiCommands

serial = Serial('/dev/ttyUSB0', 115200)

sleep(6)

fc = WiiProxy(serial)

fc.start()

for _ in range(1000):
    ident    = fc.data[MultiWiiCommands.IDENT]
    status   = fc.data[MultiWiiCommands.STATUS]
    rc       = fc.data[MultiWiiCommands.RC]
    imu      = fc.data[MultiWiiCommands.RAW_IMU]
    attitude = fc.data[MultiWiiCommands.ATTITUDE]

    print('IDENT:')
    print(f'version      = {ident.version}')
    print(f'multitype    = {ident.multitype}')
    print(f'capabilities = {ident.capabilities}')
    print(f'navi_version = {ident.navi_version}')
    
    print('STATUS:')
    print(f'cycle_time  = {status.cycle_time}')
    print(f'i2c_errors  = {status.i2c_errors}')
    print(f'sensors     = {status.sensors}')
    print(f'flag        = {status.flag}')
    print(f'global_conf = {status.global_conf}')

    print('RC:')
    print(f'roll     = {rc.roll}')
    print(f'pitch    = {rc.pitch}')
    print(f'yaw      = {rc.yaw}')
    print(f'throttle = {rc.throttle}')
    print(f'aux      = {rc.aux}')

    print('IMU:')
    print(f'acc   = {imu.acc} ')
    print(f'gyro  = {imu.gyro}')
    print(f'mag   = {imu.mag} ')

    print('ATTITUDE:')
    print(f'angle    = {attitude.angle}')
    print(f'heading  = {attitude.heading}')

    sleep(0.05)

    system('clear') # system('cls')

fc.stop()

print('Complete.')
