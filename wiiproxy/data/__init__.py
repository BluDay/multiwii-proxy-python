from dataclasses import dataclass
from typing      import NamedTuple

class Point2D(NamedTuple):
    """A tuple of x and y integer values for a 2D point."""
    x: int = 0
    y: int = 0

class Point3D(NamedTuple):
    """A tuple of x, y and z integer values for a 3D point."""
    x: int = 0
    y: int = 0
    z: int = 0
