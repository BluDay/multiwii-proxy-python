# multiwii-proxy-python

Simple and user-friendly Python 3 module for controlling drones via the MultiWii Serial Protocol (MSP) v1.

This module does not support MSP v2—or any of the newer versions.

## Documentation

The API documentation can be found on the [documentation site](https://bluday.github.io/multiwii-proxy-python/).

## Installation

Run either `pip install .` or `poetry build` to install the package:

## Usage

```python
from serial import Serial

from multiwii import MultiWii

from multiwii.commands import MSP_IDENT

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

ident = multiwii.get_data(MSP_IDENT)

print(repr(ident.multitype)) # <MultiWiiMultitype.QuadX: 3>
```

Other example usages can be found in the `examples` directory.

## Licensing

This project is licensed under the MIT license. See [LICENSE](https://github.com/BluDay/multiwii-proxy-python/blob/master/LICENSE) for more details.
