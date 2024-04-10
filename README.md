# wiiproxy

_Not functional at this time. The codebase is currently being revamped and improved._

A user-friendly and multithreaded Python 3 module for controlling _MultiWii_-based drones.

Supports only v1 of the [MultiWi Serial Protocol (MSP)](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol).

## Example usage:

```python
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

print(f'{fc.indent.multitype}') # QuadX
```
