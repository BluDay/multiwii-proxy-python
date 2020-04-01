# WiiProxy

Python 3 module for MultiWii based flight controller.

## Installation

##### Pip
```pip3 install .```

or

##### Python 3
```python3 setup.py```

## MultiWii
[MultiWii](https://github.com/multiwii) is an open source software for Arduino based flight controllers.

MultiWii uses a custom communication protocol [MultiWii Serial Protocol](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol).

## Serial communication

Some flight controllers require an FTDI chip such as the RT232RL module.

For UNIX and Linux users, ensure proper permissions to read from and write to the selected /dev/ttyUSB* file.

For Windows users, ensure administrator privileges or access to COM ports.

## Usage
```
serial = pyserial.Serial()

serial.port              = "/dev/ttyUSB0"
serial.baudrate          = 115200
serial.bytesize          = pyserial.EIGHTBITS
serial.parity            = pyserial.PARITY_NONE
serial.stopbits          = pyserial.STOPBITS_ONE
serial.write_timeout     = 3
serial.xonxoff           = False
serial.rtscts            = False
serial.dsrdtr            = False

serial.open()
```

```
from WiiProxy import MultiWii

controller = MultiWii(serial)
```

## Compatible boards

- MultiWii Crius SE 2.0
- MultiWii Crius AIO 2.0
- MultiWii PRO
