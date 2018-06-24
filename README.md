# WiiProxy

A proxy for MultiWii flight controller developed specifically for Python 3.

This "proxy" uses the [MultiWii Serial Protocol (MSP)](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol) to communicate
with the physical flight controller. The communication is established
using a serial communication.

### Installation

Enter the main directory and choose one of the following command to install the module.

##### Pip
```pip3 install .```

##### Python 3
```python3 setup.py```

### MultiWii

[MultiWii](https://github.com/multiwii) is a free and open source flight controller software made for Arduino based drones.
It was first released early 2012 and has been successful ever since drone enthusiasts, 
tinkerers and developers started building their own Arduino based drones.

MultiWii has a communication protocol for sending and receving data. This is possible
with the [MultiWii Serial Protocol (MSP)](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol).

### Why WiiProxy?

Since most developers nowadays use the programming language [Python](https://www.python.org/) and the newer version [Python 3](https://www.python.org/download/releases/3.0/), it became truly fitting and appropriate to develop WiiProxy. A simple to use and user friendly Python 3 module that allows you to effectively and safely control your MultiWii based drone.

This is the only Python 3 based module for communicating with a MultiWii flight controller. If you plan on developing a Python 3 based application for a MultiWii based drone, this module will definitely be useful.

This module can be deployed on a single-board computer such as the [Raspberry Pi](https://www.raspberrypi.org/), preferably the Raspberry Pi 3. Your single-board computer must be deployed on the drone and connected to the MultiWii flight controller via USB.

### Usage

This module is extremely easy to use and does not require a complex setup to function properly.

#### Serial communication

In order to communicate with the flight controller, you need to correctly setup a serial port which is connected to the flight controller via USB. Some flight controller boards require an FTDI chip such as the RT232RL (USB to TTY) module. The serial communication is strictly established with the [pySerial 3.4](https://pyserial.readthedocs.io/en/latest/pyserial.html) module.

##### Serial port initialization
```
serial = pyserial.Serial()

serial.port          = "/dev/ttyUSB0" # Multi-optional
serial.baudrate      = 115200
serial.bytesize      = pyserial.EIGHTBITS
serial.parity        = pyserial.PARITY_NONE
serial.stopbits      = pyserial.STOPBITS_ONE
serial.write_timeout = 3
serial.xonxoff       = False
serial.rtscts        = False
serial.dsrdtr        = False

serial.open()
```

#### Flight controller

Once you've correctly initialized a serial port, you need to create a new instance for the flight controller with your newly created serial port. You simply pass your serial object as the first parameter when creating the MultiWii instance.

##### Example
```
from WiiProxy import MultiWii

...

controller = MultiWii(serial)
```
##### Manipulation example
###### Dis/arm
```
controller.arm()

sleep(1)

channels = [1500, 1500, 1500, 1200]

controller.set_channels(channels)

controller.disarm()
```
###### Fetching metadata
```
ident = controller.get_ident()

imu = controller.get_imu()

print(ident)
print(imu)
```

### Information

This module was developed by engineer-186f[.](https://i.ytimg.com/vi/cI01_TXIMWc/hqdefault.jpg)
