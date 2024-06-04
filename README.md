
# WiiProxy

A simple and user-friendly Python 3 module for controlling _MultiWii_-based drones.

Supports only v1 of the [MultiWi Serial Protocol (MSP)](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol).

## Documentation

The API documentation can be found on the [documentation site](https://bluday.github.io/wiiproxy/).

## Installation

Run either one of these commands to install the package:

```sh
python setup.py

pip install .
```

## Usage

```python
from serial   import Serial
from wiiproxy import MultiWii

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

ident = multiwii.get_ident()

print(repr(ident.multitype)) # <MultiWiiMultitype.QuadX: 3>
```

Other example usages can be found in the `examples` directory.
