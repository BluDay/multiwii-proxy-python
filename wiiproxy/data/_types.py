from dataclasses import dataclass
from typing      import Generic, NamedTuple, TypeVar

T = TypeVar('T')

@dataclass
class Coord2D(NamedTuple, Generic[T]):
    """Represents 2D coordinates with longitude and latitude values."""
    latitude: T

    longitude: T

@dataclass
class PidValues(NamedTuple, Generic[T]):
    """Represents PID values."""
    p: T
    i: T
    d: T

@dataclass
class Point2D(NamedTuple, Generic[T]):
    """Represents a 2D point."""
    x: T
    y: T

@dataclass
class Point3D(NamedTuple, Generic[T]):
    """Represents a 3D point."""
    x: T
    y: T
    z: T
