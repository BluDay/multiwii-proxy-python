from dataclasses import dataclass
from typing      import Generic, TypeVar

T = TypeVar('T')

@dataclass
class Coord2D(Generic[T]):
    """Represents 2D coordinates with longitude and latitude values."""
    latitude: T

    longitude: T

@dataclass
class PidValues(Generic[T]):
    """Represents PID values."""
    p: T
    i: T
    d: T

@dataclass
class Point2D(Generic[T]):
    """Represents a 2D point."""
    x: T
    y: T

@dataclass
class Point3D(Generic[T]):
    """Represents a 3D point."""
    x: T
    y: T
    z: T
